import pandas as pd
# Load raw data
df = pd.read_csv('data/raw/afs_2022_financial.csv')
# Add calculated metrics
df["Profit Margin (%)"] = round((df["Net Profit (Million ZAR)"] / df["Revenue (Million ZAR)"]) * 100, 2)
df["OpEx Ratio (%)"] = round((df["Operating Expenses (Million ZAR)"] / df["Revenue (Million ZAR)"]) * 100, 2)
# Save to processed folder
df.to_csv('data/processed/afs_2022_financial_cleaned.csv', index=False)
print("Cleaned data saved to data/processed/afs_2022_financial_cleaned.csv")
