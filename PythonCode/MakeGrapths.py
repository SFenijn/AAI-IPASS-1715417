import matplotlib.pyplot as plt
import RandomDataGenerator as rgen
import linearRegression as lr



sleepdata = rgen.generate_sleep_data(14)
bedtime = sleepdata[0]
oursslept = sleepdata[1]
wakeuptime = rgen.get_wakeup_time(sleepdata)

print(bedtime)
print(oursslept)
print(wakeuptime)
rgr_line = lr.findRgrLine(lr.xlist(bedtime), bedtime)
plt.plot(lr.xlist(bedtime), bedtime, 'ro')
plt.plot(lr.xlist(bedtime), rgr_line)
plt.show()