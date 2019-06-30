import matplotlib.pyplot as plt
import numpy as np
import PatternAdjustingSimulation as inl
import linearRegression as lr
import clockFunctions as cl
import ProfileSetup as pf

seed1 = 11183
seed2 = 12345
profile1 = pf.profile_setup(60, seed2)
use_profile1 = pf.use_profile(profile1, 6)
print(use_profile1)

altered_profile1 = inl.simulate_proportional(use_profile1, 0.2, 1, 60, 6)
# altered_profile1 = inl.simulate_pid(use_profile1, 50, 6)


x = lr.xlist(altered_profile1[1][0])
y = altered_profile1[1][0]

print(y)
print(profile1[1][0])
y2 = cl.lst_strip_day(profile1[1][0])
y = cl.lst_strip_day(y)
y2 = cl.lst_strip_day(y2)


plt.plot(x, y)
plt.plot(x, y2, 'ro')
plt.yticks(np.arange(0, 24, step=1))
plt.xticks(np.arange(0, 61, step=7))
plt.show()
