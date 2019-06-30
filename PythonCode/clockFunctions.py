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


def strip_day(t):
    num = clockToNum(t)
    return numToClock(num)


def num_strip_day(t):
    time = numToClock(t)
    return clockToNum(time)


def closest(target, prediction, change):
    plus = strip_day(prediction + change)
    min = strip_day(prediction - change)
    target = clockToNum(target)

    # remove negative
    plus = clockToNum_with_day(plus)
    min = clockToNum_with_day(min)
    plus = abs(plus)
    min = abs(min)

    # check smallest
    if abs(plus - target) < abs(min - target):
        return True
    else:
        return False
