# K.Daivik Reddy
# RA2211043010021
# Exp. 5.5 – Hospital Patient Records
import pandas as pd
# Patient data
data = {
    "PatientID": [101, 102, 103, 104],
    "Name": ["Ravi", "Sita", "John", "Mary"],
    "Age": [45, 62, 70, 30],
    "BillAmount": [2000, 3500, 5000, 1500]
}
df = pd.DataFrame(data)
# Apply 10% discount for senior citizens (Age > 60)
df["Discount"] = df.apply(lambda row: row["BillAmount"] * 0.1 if row["Age"] > 60 else 0, axis=1)
df["FinalAmount"] = df["BillAmount"] - df["Discount"]
# Save to Excel
df.to_excel("hospital_records.xlsx", index=False)
print("Hospital Records:\n", df)
