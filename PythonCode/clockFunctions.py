# functions for working with a 24 clock.
from datetime import timedelta


def numToClock(t):
    return timedelta(hours=t)


def clockToNum_with_day(t):
    day_h = t.days * 24
    rest_h = t.seconds /60 /60
    return day_h + rest_h


def clockToNum(t):
    return t.seconds / 60 / 60


def lst_strip_day(list):
    newlist = []
    for i in list:
        time = numToClock(i)
        newlist.append(clockToNum(time))
    return newlist


def to_clock_strip_day(num):
    time = numToClock(num)
    num2 = clockToNum(time)
    time2 = numToClock(num2)
    return time2
