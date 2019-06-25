# functions for working with a 24 clock.

# def calcTime(time):
#     if time <= 24 and time >= 0:
import time
from datetime import timedelta


def timeToint(t):
    day_h = t.days * 24
    rest_h = t.seconds /60 /60
    return day_h + rest_h


day = timedelta(hours=27)
hour = timedelta(hours=75)
dayhour = day.days
dayint = day.seconds /60 /60
print(day)
print(hour)
newtime = day + hour
print(newtime)
print(dayint)
hours = dayhour * 24
print(dayint + hours)
print("--------------------------------")

predicted = timedelta(hours=27)
target = timedelta(hours=22)
change = timedelta(hours=1.5)
plus = predicted + change
min = predicted - change
print(plus)
print(min)
diff_p = abs(timeToint(plus) - timeToint(target))
diff_m = abs(timeToint(min) - timeToint(target))
print(diff_p)
print(diff_m)
if diff_p < diff_m:
    actiontime = plus
else:
    actiontime = min
print(actiontime)