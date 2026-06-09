# 🏦 Loan Default Risk Analyzer

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-FF4B4B?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-5.22-3F4F75?logo=plotly)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-F2C811?logo=powerbi)
![Excel](https://img.shields.io/badge/Excel-Validated-217346?logo=microsoftexcel)

> Analyzed 10,000+ real loan records to identify which customers are most likely to default — based on credit score, income, loan term, and home ownership. Built an end-to-end analytics pipeline using Python, PostgreSQL, Excel, Power BI and a live Streamlit web dashboard.

---

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Business Problem](#business-problem)
- [Tools Used](#tools-used)
- [Project Workflow](#project-workflow)
- [Key Findings](#key-findings)
- [Dashboard Preview](#dashboard-preview)
- [Folder Structure](#folder-structure)
- [How to Run](#how-to-run)
- [Skills Demonstrated](#skills-demonstrated)

---

## 📖 Project Overview

Banks lose crores of rupees every year because some customers fail to repay loans. This project simulates the work of a real credit risk analyst — cleaning messy raw data, querying patterns using SQL, validating findings in Excel, and presenting insights through interactive dashboards.

The final output is a **live Streamlit web dashboard** connected to PostgreSQL that auto-refreshes every 30 seconds — simulating a real production analytics system.

---

## 💼 Business Problem

**"Which customers are most likely to default on their loan — and why?"**

A bank needs to answer this question before approving any loan. This project identifies the key risk factors and high-risk customer segments so the bank can make smarter lending decisions.

---

## 🛠 Tools Used

| Tool | Purpose |
|------|---------|
| **Python** (pandas, numpy, matplotlib, seaborn) | Data cleaning and feature engineering |
| **PostgreSQL + pgAdmin** | SQL querying and pattern analysis |
| **Microsoft Excel** | Cross-validation using pivot tables |
| **Power BI** | Interactive business dashboard |
| **Streamlit + Plotly** | Live web dashboard connected to database |

---

## 🔄 Project Workflow

```
raw CSV data
     ↓
Phase 1 — Data Collection
     ↓
Phase 2 — Python Cleaning (01_data_cleaning.ipynb)
   • Removed junk rows and impossible credit scores
   • Filled missing values using median / business logic
   • Removed outliers using IQR method
   • Converted text columns to numbers
   • Created 3 new features: debt_to_income, credit_risk_tier, default
     ↓
Phase 3 — SQL Analysis (pgAdmin / PostgreSQL)
   • 7 business queries written in pgAdmin directly
   • Default rate by loan term, home ownership, purpose, risk tier
   • Compared defaulters vs non-defaulters profile
   • Identified top 10 highest risk customers
     ↓
Phase 4 — Excel Validation (loan_analysis.xlsx)
   • 3 pivot tables cross-validating SQL findings
   • Conditional formatting highlighting high risk segments
   • Summary sheet with all key metrics
     ↓
Phase 5 — Power BI Dashboard (loan_dashboard.pbix)
   • 5 visuals with 3 interactive slicers
     ↓
Phase 6 — Live Streamlit Dashboard (dashboard.py)
   • Connected directly to PostgreSQL
   • Auto-refreshes every 30 seconds
   • Sidebar filters, KPI cards, charts, risk table
```

---

## 📊 Key Findings

- **Overall default rate** — X% of customers defaulted
- **Credit Risk Tier** — Very High Risk customers defaulted at Xx the rate of Low Risk customers
- **Loan Term** — Long Term loans showed higher default rates than Short Term
- **Home Ownership** — Renters defaulted more than homeowners showing lower financial stability
- **Credit Score Gap** — Average credit score of defaulters was significantly lower than non-defaulters confirming credit score as the strongest predictor

> Replace X values above with your actual numbers from SQL Query results

---

## 📸 Dashboard Preview

### Power BI Dashboard
![Power BI Dashboard](dashboard_screenshot.png)

### Streamlit Live Dashboard
![Streamlit Dashboard](streamlit_screenshot.png)

> Add your actual screenshots to the project folder and they will appear here automatically

---

## 📁 Folder Structure

```
loan_default_project/
│
├── 📓 01_data_cleaning.ipynb      # Python data cleaning notebook
├── 🐍 02_load_to_postgres.py      # Loads clean data into PostgreSQL
├── 🌐 dashboard.py                # Live Streamlit web dashboard
│
├── 📂 data/
│   ├── credit_test.csv            # Original raw dataset
│   └── clean_loans.csv            # Cleaned output from Phase 2
│
├── 📂 outputs/
│   ├── data_overview.png          # Charts from Python cleaning
│   ├── loan_analysis.xlsx         # Excel pivot table validation
│   └── loan_dashboard.pbix        # Power BI dashboard file
│
├── 📄 requirements.txt            # All Python dependencies
└── 📄 README.md                   # This file
```

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/loan-default-risk-analyzer.git
cd loan-default-risk-analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up PostgreSQL
- Install PostgreSQL and create a database called `loan_db`
- Update your password in `02_load_to_postgres.py` and `dashboard.py`

### 4. Load data into PostgreSQL
```bash
python 02_load_to_postgres.py
```

### 5. Run the live Streamlit dashboard
```bash
streamlit run dashboard.py
```

Opens automatically at `http://localhost:8501`

---

## ✅ Skills Demonstrated

- **Data Cleaning** — handling nulls, outliers, encoding, feature engineering
- **SQL** — GROUP BY, CASE WHEN, aggregations, filtering, subqueries
- **Excel** — pivot tables, conditional formatting, cross-validation
- **Power BI** — DAX measures, interactive slicers, KPI cards
- **Streamlit** — live web dashboard connected to production database
- **Business Thinking** — every analysis tied to a real banking decision
- **Professional Practices** — requirements.txt, documented code, README

---

## 👤 Author

**Your Name** Deval Pathak
- LinkedIn: [linkedin.com/in/yourprofile](https://# 🏦 Loan Default Risk Analyzer

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-FF4B4B?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-5.22-3F4F75?logo=plotly)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-F2C811?logo=powerbi)
![Excel](https://img.shields.io/badge/Excel-Validated-217346?logo=microsoftexcel)

> Analyzed 10,000+ real loan records to identify which customers are most likely to default — based on credit score, income, loan term, and home ownership. Built an end-to-end analytics pipeline using Python, PostgreSQL, Excel, Power BI and a live Streamlit web dashboard.

---

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Business Problem](#business-problem)
- [Tools Used](#tools-used)
- [Project Workflow](#project-workflow)
- [Key Findings](#key-findings)
- [Dashboard Preview](#dashboard-preview)
- [Folder Structure](#folder-structure)
- [How to Run](#how-to-run)
- [Skills Demonstrated](#skills-demonstrated)

---

## 📖 Project Overview

Banks lose crores of rupees every year because some customers fail to repay loans. This project simulates the work of a real credit risk analyst — cleaning messy raw data, querying patterns using SQL, validating findings in Excel, and presenting insights through interactive dashboards.

The final output is a **live Streamlit web dashboard** connected to PostgreSQL that auto-refreshes every 30 seconds — simulating a real production analytics system.

---

## 💼 Business Problem

**"Which customers are most likely to default on their loan — and why?"**

A bank needs to answer this question before approving any loan. This project identifies the key risk factors and high-risk customer segments so the bank can make smarter lending decisions.

---

## 🛠 Tools Used

| Tool | Purpose |
|------|---------|
| **Python** (pandas, numpy, matplotlib, seaborn) | Data cleaning and feature engineering |
| **PostgreSQL + pgAdmin** | SQL querying and pattern analysis |
| **Microsoft Excel** | Cross-validation using pivot tables |
| **Power BI** | Interactive business dashboard |
| **Streamlit + Plotly** | Live web dashboard connected to database |

---

## 🔄 Project Workflow

```
raw CSV data
     ↓
Phase 1 — Data Collection
     ↓
Phase 2 — Python Cleaning (01_data_cleaning.ipynb)
   • Removed junk rows and impossible credit scores
   • Filled missing values using median / business logic
   • Removed outliers using IQR method
   • Converted text columns to numbers
   • Created 3 new features: debt_to_income, credit_risk_tier, default
     ↓
Phase 3 — SQL Analysis (pgAdmin / PostgreSQL)
   • 7 business queries written in pgAdmin directly
   • Default rate by loan term, home ownership, purpose, risk tier
   • Compared defaulters vs non-defaulters profile
   • Identified top 10 highest risk customers
     ↓
Phase 4 — Excel Validation (loan_analysis.xlsx)
   • 3 pivot tables cross-validating SQL findings
   • Conditional formatting highlighting high risk segments
   • Summary sheet with all key metrics
     ↓
Phase 5 — Power BI Dashboard (loan_dashboard.pbix)
   • 5 visuals with 3 interactive slicers
     ↓
Phase 6 — Live Streamlit Dashboard (dashboard.py)
   • Connected directly to PostgreSQL
   • Auto-refreshes every 30 seconds
   • Sidebar filters, KPI cards, charts, risk table
```

---

## 📊 Key Findings

- **Overall default rate** — X% of customers defaulted
- **Credit Risk Tier** — Very High Risk customers defaulted at Xx the rate of Low Risk customers
- **Loan Term** — Long Term loans showed higher default rates than Short Term
- **Home Ownership** — Renters defaulted more than homeowners showing lower financial stability
- **Credit Score Gap** — Average credit score of defaulters was significantly lower than non-defaulters confirming credit score as the strongest predictor

> Replace X values above with your actual numbers from SQL Query results

---

## 📸 Dashboard Preview

### Power BI Dashboard
![Power BI Dashboard](dashboard_screenshot.png)

### Streamlit Live Dashboard
![Streamlit Dashboard](streamlit_screenshot.png)

> Add your actual screenshots to the project folder and they will appear here automatically

---

## 📁 Folder Structure

```
loan_default_project/
│
├── 📓 01_data_cleaning.ipynb      # Python data cleaning notebook
├── 🐍 02_load_to_postgres.py      # Loads clean data into PostgreSQL
├── 🌐 dashboard.py                # Live Streamlit web dashboard
│
├── 📂 data/
│   ├── credit_test.csv            # Original raw dataset
│   └── clean_loans.csv            # Cleaned output from Phase 2
│
├── 📂 outputs/
│   ├── data_overview.png          # Charts from Python cleaning
│   ├── loan_analysis.xlsx         # Excel pivot table validation
│   └── loan_dashboard.pbix        # Power BI dashboard file
│
├── 📄 requirements.txt            # All Python dependencies
└── 📄 README.md                   # This file
```

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/loan-default-risk-analyzer.git
cd loan-default-risk-analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up PostgreSQL
- Install PostgreSQL and create a database called `loan_db`
- Update your password in `02_load_to_postgres.py` and `dashboard.py`

### 4. Load data into PostgreSQL
```bash
python 02_load_to_postgres.py
```

### 5. Run the live Streamlit dashboard
```bash
streamlit run dashboard.py
```

Opens automatically at `http://localhost:8501`

---

## ✅ Skills Demonstrated

- **Data Cleaning** — handling nulls, outliers, encoding, feature engineering
- **SQL** — GROUP BY, CASE WHEN, aggregations, filtering, subqueries
- **Excel** — pivot tables, conditional formatting, cross-validation
- **Power BI** — DAX measures, interactive slicers, KPI cards
- **Streamlit** — live web dashboard connected to production database
- **Business Thinking** — every analysis tied to a real banking decision
- **Professional Practices** — requirements.txt, documented code, README

---

## 👤 Author

**Your Name**
- LinkedIn: [https://linkedin.com/in/devalpathak-298772225](https://www.linkedin.com/in/deval-pathak-298772225/)
- Email: devalpathak30@gmail.com

---

## 📃 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Built with 💙 as part of Data Analyst Portfolio — 2026
</p>)
- GitHub: [github.com/yourusername](https://github.com/yourusername)
- Email: your.email@gmail.com

---

## 📃 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Built with 💙 as part of Data Analyst Portfolio — 2026
</p>
