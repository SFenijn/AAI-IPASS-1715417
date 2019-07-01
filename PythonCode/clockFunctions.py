# functions for working with a 24 clock.
from datetime import timedelta


def numToClock(t):
    """"int/float to datetime"""
    return timedelta(hours=t)


def clockToNum_with_day(t):
    """"datetime to float with datetime days"""
    day_h = t.days * 24
    rest_h = t.seconds /60 /60
    return day_h + rest_h


def clockToNum(t):
    """"datetime to float without datetime days"""
    return t.seconds / 60 / 60


def lst_strip_day(list):
    """"strip datetime day from float from a list of floats"""
    newlist = []
    for i in list:
        time = numToClock(i)
        newlist.append(clockToNum(time))
    return newlist


def to_clock_strip_day(num):
    """"strip datetime day from float and to datetime"""
    time = numToClock(num)
    num2 = clockToNum(time)
    time2 = numToClock(num2)
    return time2


def strip_day(t):
    """strip datatime day from a datetime"""
    num = clockToNum(t)
    return numToClock(num)


def num_strip_day(t):
    """strip datetime day from float"""
    time = numToClock(t)
    return clockToNum(time)


def closest(target, prediction, change):
    """"find if plus or min is closest to target"""
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
