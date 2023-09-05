import pandas as pd

# Read the Excel file
df = pd.read_excel('data/EADA_2022.xlsx', sheet_name='EADA_2022')

# Save the data frame to CSV file
df.to_csv('data/EADA_2022.csv', index=False)

print("CSV file created successfully.")