import pandas as pd

# Read CSV files into pandas DataFrames
df_a = pd.read_csv('./UntitledspreadsheetSheet1.csv')  # Assuming file_a.csv contains name and phone number
df_b = pd.read_csv('./UntitledspreadsheetSheet2.csv')  # Assuming file_b.csv contains only names

# Merge DataFrames on the "name" column
merged_df = pd.merge(df_a, df_b, on='Name', how='inner')

#tst2

# Print the merged DataFrame with only the "name" and "phone number" columns
print(merged_df[['Name', 'Phone']])
