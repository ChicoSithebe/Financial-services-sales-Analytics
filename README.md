# Financial Services Sales Analytics

An end-to-end data analytics project analyzing financial metrics in South Africa's financial services sector. Built using real-world structured data, Python for data cleaning, and Power BI for data visualization.  

This project demonstrates data engineering, ETL, and business intelligence skills using Microsoft Azure, GitHub, and open datasets.

---

## Project Objectives

- Clean and analyze sales and financial performance data

- Calculate key KPIs: Profit Margin %, Operating Expense Ratio %

- Prepare data for visual analytics and dashboards

- Build an interactive Power BI report

---

## Tech Stack

- **Python (pandas)** – Data cleaning & transformation

- **GitHub** – Version control and portfolio hosting

- **Azure Data Factory** – (optional) for ETL pipelines

- **Power BI** – KPI dashboards and insights

- **CSV files** – Based on Annual Financial Statistics data from Stats SA

---

## Folder Structure 
financial-services-sales-analytics/
├── data/
│   ├── raw/            # Original AFS dataset
│   └── processed/      # Cleaned dataset with new metrics
├── scripts/            # Python script for cleaning
├── notebooks/          # Optional EDA notebooks
├── reports/            # Power BI dashboards
├── README.md
---
## KPI Calculations
- **Profit Margin (%)** = (Net Profit ÷ Revenue) × 100  
- **Operating Expense Ratio (%)** = (Operating Expenses ÷ Revenue) × 100
---
## How to Run This Project
1. Clone the repo: 
  ```bash
git clone https://github.com/ChicoSithebe/Financial-services-sales-Analytics.git 

2. Run the cleaning script
 
python scripts/clean_afs_data.py
03. Output file:

	•	Check data/processed/afs_2022_financial_cleaned.csv .

  Power BI Dashboard
Coming soon:
• Visuals for Revenue, Profit Margin, OpEx Ratio by Industry and Year
• Top financial service sectors by performance
• Year-over-Year revenue trends
Dashboard will be added under reports/dashboard.pbix.
⸻
License
This project is licensed under the MIT License.
⸻
Author
Chico Sithebe
[LinkedIn Profile](https://www.linkedin.com/in/chico-sithebe)

