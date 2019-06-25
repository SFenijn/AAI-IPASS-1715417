# functions for working with a 24 clock.

# def calcTime(time):
#     if time <= 24 and time >= 0:
import time
from datetime import timedelta

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