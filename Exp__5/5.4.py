import pandas as pd
import numpy as np

# Student list
students = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Randomly generate attendance (Present = 1, Absent = 0)
attendance = np.random.randint(0, 2, size=len(students))

# Create DataFrame
df = pd.DataFrame({
    "Student": students,
    "Attendance": ["Present" if x == 1 else "Absent" for x in attendance]
})

# Save to Excel
df.to_excel("attendance.xlsx", index=False)

print("Attendance List:\n", df)
