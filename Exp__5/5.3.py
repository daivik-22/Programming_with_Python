# K.Daivik Reddy
# RA2211043010021
# Exp. 5.3 – Weather Data Analysis using NumPy
import numpy as np
# Example: Assume weather.txt contains daily temperatures
# Example content of weather.txt:
# 30
# 32
# 29
# 35
# 31
# Load data
data = np.loadtxt("weather.txt")
print("Weather Data:", data)
# Basic analysis
print("Max Temperature:", np.max(data))
print("Min Temperature:", np.min(data))
print("Average Temperature:", np.mean(data))
print("Standard Deviation:", np.std(data))
