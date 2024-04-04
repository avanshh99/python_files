import pandas as pd

# Import CSV file into a DataFrame
df = pd.read_csv('emoji.csv')

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Display basic information about the DataFrame
print("\nInfo about the DataFrame:")
print(df.info())

# Display summary statistics of numerical columns
print("\nSummary statistics:")
print(df.describe())

# Select a specific column and display its unique values
print("\nUnique values in the 'Sentiment score' column:")
print(df['Sentiment score'].unique())

# Filter rows based on a condition
print("\nRows where 'Quantity' is greater than 10:")
print(df[df['Occurrences'] > 7879])

# Grouping data by a column and calculating aggregate statistics
print("\nTotal quantity sold per category:")
print(df.groupby('Category')['Quantity'].sum())

# Sorting the DataFrame by a column
print("\nDataFrame sorted by 'Price' in descending order:")
print(df.sort_values(by='Price', ascending=False))

# Writing the modified DataFrame back to a CSV file
df.to_csv('modified_example.csv', index=False)

print("\nOperations completed successfully.")
