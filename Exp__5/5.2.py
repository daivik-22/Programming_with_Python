import pandas as pd

# Load dataset (you can replace with your own CSV file)
df = pd.read_csv("sample_dataset.csv")

# Display first 5 rows
print("Head of dataset:\n", df.head())

# Display last 5 rows
print("\nTail of dataset:\n", df.tail())

# Summary statistics
print("\nSummary Statistics:\n", df.describe())

# Info of dataset
print("\nDataset Info:")
print(df.info())
