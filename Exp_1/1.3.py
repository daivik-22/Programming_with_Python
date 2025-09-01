# Exp 1.3
from math import *

daivi_dc = 0.2
daivik_ad = 1.2

a_daivi = pi * 0.11**2
sc_daivi = 1000.0 / 3600  # conversion factor

v_daivik = 120 * sc_daivi
u_daivik = 10 * sc_daivi

# Hard kick
daivik_f = 0.5 * daivi_dc * daivik_ad * a_daivi * v_daivik**2
print('Hard kick:', daivik_f)

# Soft kick
daivik_f1 = 0.5 * daivi_dc * daivik_ad * a_daivi * u_daivik**2
print('Soft kick:', daivik_f1)
