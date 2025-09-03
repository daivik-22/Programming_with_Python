# K.Daivik Reddy
# RA2211043010021
# Exp. 5.1 – Create an Excel Sheet using Pandas
import pandas as pd
# Sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [23, 25, 22, 24],
    "Marks": [88, 92, 79, 85]
}
# Create DataFrame
df = pd.DataFrame(data)
# Save to Excel
df.to_excel("students.xlsx", index=False)
print("Excel file 'students.xlsx' created successfully!")
print(df)
