# Exp 1.2
from math import *

daivik_x = 0.5
daivik_g = 9.81
daivik_u = 10
daivik_v0 = 10 / 3.6
daivik_rad = (pi / 180) * 45  # converting degrees to radians

daivik_y = (daivik_x * tan(daivik_rad)) - (daivik_g * (daivik_x**2)) / ((2 * (daivik_v0**2)) * (cos(daivik_rad)**2))

print("Projectile Y:", daivik_y)
