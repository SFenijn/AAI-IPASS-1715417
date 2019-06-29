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
    print("plus:", plus - target)
    print("min:", min -target)
    target = clockToNum(target)
    # remove negative
    plus = clockToNum_with_day(plus)
    min = clockToNum_with_day(min)
    plus = abs(plus)
    min = abs(min)
    print(plus - target, min - target)
    # check smallest
    if abs(plus - target) < abs(min - target):
        return True
    else:
        return False


# day = timedelta(hours=24)
#
# time1 = timedelta(hours=20)
# time2 = timedelta(hours=18)
# time1 = time1-day
# time2 = time2-day
# print(time1, time2)
# print(time1 < time2)
#
# time1 = timedelta(hours=20)
# time2 = timedelta(hours=18)
# time1 = time1-day
# time2 = time2-day
# time1 = clockToNum(time1)
# time2 = clockToNum(time2)
# print(time1, time2)
# print(time1 < time2)
#
# time1 = timedelta(hours=20)
# time2 = timedelta(hours=18)
# time1 = time1-day
# time2 = time2-day
# time1 = clockToNum_with_day(time1)
# time2 = clockToNum_with_day(time2)
# print(time1, time2)
# print(time1 < time2)
#
# time1 = timedelta(hours=20)
# time2 = timedelta(hours=18)
# time1 = time1-day
# time2 = time2-day
# time1 = clockToNum_with_day(time1)
# time2 = clockToNum_with_day(time2)
# time1 = abs(time1)
# time2 = abs(time2)
# print(time1, time2)
# print(time1 < time2)
#
# time1 = timedelta(hours=20)
# time2 = timedelta(hours=18)
# time1 = time1-day
# time2 = time2-day
# print(time1, time2)
# print(time1 < time2)
#
# time1 = timedelta(hours=20)
# time2 = timedelta(hours=18)
# time1 = clockToNum(time1)
# time2 = clockToNum(time2)
# print(time1, time2)
# print(time1 < time2)
#
# time1 = timedelta(hours=20)
# time2 = timedelta(hours=18)
# time1 = clockToNum_with_day(time1)
# time2 = clockToNum_with_day(time2)
# print(time1, time2)
# print(time1 < time2)
#
# time1 = timedelta(hours=20)
# time2 = timedelta(hours=18)
# time1 = clockToNum_with_day(time1)
# time2 = clockToNum_with_day(time2)
# time1 = abs(time1)
# time2 = abs(time2)
# print(time1, time2)
# print(time1 < time2)
# testtime = timedelta(hours=24)
# target1 = timedelta(hours=2)
# target2 = timedelta(hours=23)
# prediction1 = timedelta(hours=23)
# prediction2 = timedelta(hours=1.5)
# change = timedelta(hours=1.5)
#
# plus1 = strip_day(prediction1 + change)
# plus2 = strip_day(prediction2 + change)
# min1 = strip_day(prediction1 - change)
# min2 = strip_day(prediction2 - change)
#
# list1 = [plus1, min1]
# list2 = [plus2, min2]
#
# print("test1:")
# print("target1:", target1)
# print("prediction1:", prediction1)
# print("plus:", plus1,"min:", min1)
# print(plus1 - target1)
# print(min1 - target1)
# print(closest(target1, list1),"target:", target1)
# if plus1 - target1 < min1 - target1:
#     print("plus", plus1)
# else:
#     print("min", min1)
# print()
#
#
# print("\ntest2:")
# print("target2:", target2)
# print("prediction2:", prediction2)
# print("plus:", plus2,"min:", min2)
# print(plus2 - target2)
# print(min2 - target2)
# print(closest(target2, list2),"target:", target2)
# if plus2 - target2 < min2 - target2:
#     print("plus", plus2)
# else:
#     print("min", min2)
# print()
