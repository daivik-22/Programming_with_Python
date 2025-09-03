import pandas as pd

# Create initial book data
data = {
    "BookID": [1, 2, 3, 4],
    "Title": ["Python Basics", "Data Science 101", "Machine Learning", "AI for Everyone"],
    "Author": ["Smith", "Johnson", "Williams", "Brown"],
    "Status": ["Available", "Issued", "Available", "Available"]
}

df = pd.DataFrame(data)

print("Initial Library Data:\n", df)

# Update status of a book (example: issuing BookID=3)
df.loc[df["BookID"] == 3, "Status"] = "Issued"

# Save updated data
df.to_csv("library.txt", index=False, sep="\t")

print("\nUpdated Library Data:\n", df)
