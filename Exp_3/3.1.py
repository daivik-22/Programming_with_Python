# Expt 3.1 – Student Grade Evaluation
def grade(marks):
    if marks >= 90: return "A"
    elif marks >= 75: return "B"
    elif marks >= 50: return "C"
    else: return "F"

print("Grade:", grade(85))
