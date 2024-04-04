import pandas as pd

# Sample data as lists
data = [
    ['John', 25, 'New York'],
    ['Alice', 30, 'Los Angeles'],
    ['Bob', 35, 'Chicago']
]

# Define column names
columns = ['Name', 'Age', 'City']

# Create DataFrame from the data and columns
df = pd.DataFrame(data, columns=columns)

# Display DataFrame
print("DataFrame:")
print(df)

# Write DataFrame to CSV file
df.to_csv('data.csv', index=False)
print("DataFrame written to CSV file 'data.csv'.")

# Read DataFrame from CSV file
df_read = pd.read_csv('data.csv')

# Display DataFrame read from CSV file
print("\nDataFrame read from CSV file:")
print(df_read)

# Accessing DataFrame elements
print("\nAccessing DataFrame elements:")
print("First row:")
print(df.iloc[0])  # Access first row
print("Age column:")
print(df['Age'])   # Access Age column

# Filtering DataFrame
print("\nFiltering DataFrame:")
filtered_df = df[df['Age'] > 25]  # Filter rows where Age > 25
print(filtered_df)

# Adding a new column
print("\nAdding a new column:")
df['Country'] = ['USA', 'USA', 'USA']  # Add new 'Country' column
print(df)

# Sorting DataFrame
print("\nSorting DataFrame:")
sorted_df = df.sort_values(by='Age', ascending=False)  # Sort DataFrame by Age in descending order
print(sorted_df)

# Grouping and aggregation
print("\nGrouping and aggregation:")
grouped_df = df.groupby('City').agg({'Age': 'mean'})  # Group by City and calculate average Age
print(grouped_df)
