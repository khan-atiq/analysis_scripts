import pandas as pd

# Read CSV files into pandas DataFrames
df_a = pd.read_csv('./export.csv')  # Assuming export10.csv contains name, mobile number, and application ID
df_b = pd.read_csv('./UntitledspreadsheetSheet3.csv')  # Assuming UntitledspreadsheetSheet3.csv contains only application IDs

# Merge DataFrames on the "Application ID" column
merged_df = pd.merge(df_a, df_b, on='Application ID', how='inner')

# Group by "Application ID" and count the occurrences
application_id_count = merged_df['Application ID'].value_counts()

# Iterate over each row in the merged DataFrame and print name with corresponding mobile number, application ID, and count
for index, row in merged_df.iterrows():
    print("Application ID:", row['Application ID'])
    print("Mobile:", row['mobile'])
    print("Name:", row['name'])
    print("Count:", application_id_count[row['Application ID']])  # Print the count of the current application ID
    print()  # Add an empty line for readability