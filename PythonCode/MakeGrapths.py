import matplotlib.pyplot as plt
import numpy as np
import patternTesting as pt
import linearRegression as lr
import influencePattern as ip
import clockFunctions as cl

seed1 = 11185
seed2 = 12345
profile1 = ip.profile_setup(60, seed2)
use_profile1 = pt.use_profile(profile1)
altered_profile1 = pt.simulate_usecase(use_profile1, 0.5, 1, 60)
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
