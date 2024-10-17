import pandas as pd
import os

# Specify the directory containing the CSV files
csv_directory = 'csvs'

# List all files in the directory
files = os.listdir(csv_directory)

# Initialize an empty list to store DataFrames
df_list = []

# Loop over the files
for file in files:
    # Check if the file is a CSV file
    if file.endswith('.csv'):
        # Read the CSV file into a DataFrame
        df = pd.read_csv(os.path.join(csv_directory, file))
        df['Category']=file
        # Append the DataFrame to the list
        df_list.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
combined_df = pd.concat(df_list, ignore_index=True)

# Save the combined DataFrame to an Excel file
combined_df.to_excel('combined_data.xlsx', index=False)

print("Data has been successfully saved to 'combined_data.xlsx'.")