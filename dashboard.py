import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine
import time

# ─────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Loan Default Risk Analyzer",
    page_icon="🏦",
    layout="wide"
)

# ─────────────────────────────────────────
# DATABASE CONNECTION
# ─────────────────────────────────────────
@st.cache_resource
def get_engine():
    return create_engine(
        "postgresql://postgres:pass123@localhost:5432/loan_db"
        # ↑ replace yourpassword with your actual password
    )

# ─────────────────────────────────────────
# LOAD LIVE DATA FROM POSTGRESQL
# ─────────────────────────────────────────
@st.cache_data(ttl=30)  # refreshes every 30 seconds automatically
def load_data():
    engine = get_engine()
    query = """
        SELECT 
            "Loan ID",
            "Credit Score",
            "Annual Income",
            "Term",
            "Home Ownership",
            "Monthly Debt",
            "Number of Credit Problems",
            "Bankruptcies",
            debt_to_income,
            credit_risk_tier,
            "default"
        FROM loans
    """
    df = pd.read_sql(query, engine)
    return df

# ─────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────
st.markdown("""
    <h1 style='color:#1a3c6e;'>
        🏦 Loan Default Risk Analyzer
    </h1>
    <p style='color:gray; margin-top:-15px;'>
        Live dashboard connected to PostgreSQL • Auto-refreshes every 30 seconds
    </p>
    <hr/>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────
with st.spinner("Loading live data from database..."):
    df = load_data()

# ─────────────────────────────────────────
# SIDEBAR FILTERS
# ─────────────────────────────────────────
st.sidebar.title("🔎 Filters")
st.sidebar.markdown("Use filters to explore default risk by segment")

# Filter 1 — Term
term_options = ["All"] + sorted(df["Term"].dropna().unique().tolist())
selected_term = st.sidebar.selectbox("Loan Term", term_options)

# Filter 2 — Home Ownership
ownership_options = ["All"] + sorted(df["Home Ownership"].dropna().unique().tolist())
selected_ownership = st.sidebar.selectbox("Home Ownership", ownership_options)

# Filter 3 — Credit Risk Tier
tier_options = ["All"] + sorted(df["credit_risk_tier"].dropna().unique().tolist())
selected_tier = st.sidebar.selectbox("Credit Risk Tier", tier_options)

# Apply filters
filtered_df = df.copy()
if selected_term != "All":
    filtered_df = filtered_df[filtered_df["Term"] == selected_term]
if selected_ownership != "All":
    filtered_df = filtered_df[filtered_df["Home Ownership"] == selected_ownership]
if selected_tier != "All":
    filtered_df = filtered_df[filtered_df["credit_risk_tier"] == selected_tier]

# Show filter summary
st.sidebar.markdown("---")
st.sidebar.metric("Filtered Customers", f"{len(filtered_df):,}")

# ─────────────────────────────────────────
# KPI CARDS — ROW 1
# ─────────────────────────────────────────
st.markdown("### 📊 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

total_customers   = len(filtered_df)
total_defaulters  = filtered_df["default"].sum()
default_rate      = (total_defaulters / total_customers * 100) if total_customers > 0 else 0
avg_credit_score  = filtered_df["Credit Score"].mean()

col1.metric(
    label="Total Customers",
    value=f"{total_customers:,}"
)
col2.metric(
    label="Total Defaulters",
    value=f"{int(total_defaulters):,}"
)
col3.metric(
    label="Overall Default Rate",
    value=f"{default_rate:.1f}%"
)
col4.metric(
    label="Avg Credit Score",
    value=f"{avg_credit_score:.0f}"
)

st.markdown("---")

# ─────────────────────────────────────────
# ROW 2 — Bar Chart + Donut Chart
# ─────────────────────────────────────────
col_left, col_right = st.columns([3, 2])

# ── Bar Chart: Default Rate by Risk Tier ──
with col_left:
    st.markdown("#### Default Rate by Credit Risk Tier")

    tier_data = (
        filtered_df.groupby("credit_risk_tier")["default"]
        .agg(["sum", "count"])
        .reset_index()
    )
    tier_data.columns = ["Risk Tier", "Defaulters", "Total"]
    tier_data["Default Rate %"] = (
        tier_data["Defaulters"] / tier_data["Total"] * 100
    ).round(2)

    # Color map
    color_map = {
        "Very High Risk": "#e74c3c",
        "High Risk":      "#e67e22",
        "Medium Risk":    "#f1c40f",
        "Low Risk":       "#2ecc71"
    }

    fig_bar = px.bar(
        tier_data,
        x="Default Rate %",
        y="Risk Tier",
        orientation="h",
        color="Risk Tier",
        color_discrete_map=color_map,
        text="Default Rate %",
        title=""
    )
    fig_bar.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
    fig_bar.update_layout(
        showlegend=False,
        xaxis_title="Default Rate %",
        yaxis_title="",
        height=300,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# ── Donut Chart: Default Rate by Loan Term ──
with col_right:
    st.markdown("#### Default Rate by Loan Term")

    term_data = (
        filtered_df.groupby("Term")["default"]
        .agg(["sum", "count"])
        .reset_index()
    )
    term_data.columns = ["Term", "Defaulters", "Total"]
    term_data["Default Rate %"] = (
        term_data["Defaulters"] / term_data["Total"] * 100
    ).round(2)

    fig_donut = px.pie(
        term_data,
        names="Term",
        values="Default Rate %",
        hole=0.5,
        color_discrete_sequence=["#1a3c6e", "#3498db"]
    )
    fig_donut.update_layout(
        height=300,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig_donut, use_container_width=True)

st.markdown("---")

# ─────────────────────────────────────────
# ROW 3 — Scatter Plot
# ─────────────────────────────────────────
st.markdown("#### Credit Score vs Annual Income — Colored by Default Status")

scatter_df = filtered_df.copy()
scatter_df["Status"] = scatter_df["default"].map({1: "Defaulted", 0: "Paid"})

fig_scatter = px.scatter(
    scatter_df.sample(min(2000, len(scatter_df))),
    x="Annual Income",
    y="Credit Score",
    color="Status",
    color_discrete_map={"Defaulted": "#e74c3c", "Paid": "#2ecc71"},
    opacity=0.6,
    title=""
)
fig_scatter.update_layout(
    height=350,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)"
)
st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("---")

# ─────────────────────────────────────────
# ROW 4 — High Risk Customers Table
# ─────────────────────────────────────────
st.markdown("#### 🚨 Highest Risk Customers")

high_risk = (
    filtered_df[filtered_df["default"] == 1]
    [[
        "Loan ID", "Credit Score", "Annual Income",
        "Term", "Home Ownership", "credit_risk_tier",
        "Number of Credit Problems", "Bankruptcies",
        "debt_to_income"
    ]]
    .sort_values(
        ["Number of Credit Problems", "Bankruptcies"],
        ascending=False
    )
    .head(20)
    .reset_index(drop=True)
)

# Color rows by risk tier
def highlight_risk(row):
    if row["credit_risk_tier"] == "Very High Risk":
        return ["background-color: #fde8e8"] * len(row)
    elif row["credit_risk_tier"] == "High Risk":
        return ["background-color: #fef3e2"] * len(row)
    else:
        return [""] * len(row)

st.dataframe(
    high_risk.style.apply(highlight_risk, axis=1),
    use_container_width=True,
    height=400
)

# ─────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────
st.markdown("---")
st.markdown("""
    <p style='text-align:center; color:gray; font-size:12px;'>
        Loan Default Risk Analyzer • Built with Python, PostgreSQL, Streamlit & Plotly • 2026
    </p>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# AUTO REFRESH
# ─────────────────────────────────────────
time.sleep(30)
st.rerun()