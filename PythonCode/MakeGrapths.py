import matplotlib.pyplot as plt
import numpy as np
import patternTesting as pt
import linearRegression as lr
import influencePattern as ip
import clockFunctions as cl


profile1 = ip.profile_setup(60)
use_profile1 = pt.use_profile(profile1)
altered_profile1 = pt.simulate_usecase(use_profile1, 0.3, 1, 60)
x = lr.xlist(altered_profile1[1][0])
y = altered_profile1[1][0]
y2 = cl.lst_strip_day(profile1[1][0])
y = cl.lst_strip_day(y)
y2 = cl.lst_strip_day(y2)

print(y)
print(y2)
plt.plot(x, y)
plt.plot(x, y2, 'ro')
plt.yticks(np.arange(0, 23, step=1))
plt.show()
