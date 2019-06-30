import math


def findMean(list):
    """":returns mean"""
    total = 0
    size = 0
    for i in list:
        total += i
        size += 1
    return total / size


def findMedian(list):
    """":returns median"""
    list.sort()
    if len(list) % 2 != 0:
        return list[int((len(list)/2) - 1.5)]
    else:
        return list[int((((len(list)/2)) + ((len(list)/2)-1)) / 2)]


def findVarians(list):
    """":returns varians"""
    mean = findMean(list)
    total = 0
    count = 0
    for i in list:
        total += (i - mean) * (i - mean)
        count += 1
    return total / count


def findStandardDeviation(list):
    """":returns standard deviation"""
    varians = findVarians(list)
    return math.sqrt(varians)


def findMeanSquerd(list):
    """":returns mean^2"""
    total = 0
    size = 0
    for i in list:
        total += i * i
        size += 1
    return total / size


def findMeanXY(listX, listY):
    """":returns mean XY"""
    total = 0
    size = 0
    for i in range(len(listX)):
        total += listX[i] * listY[i]
        size += 1
    return total / size


def findM(listX, listY):
    """":returns m"""
    meanX = findMean(listX)
    meanY = findMean(listY)
    meanXY = findMeanXY(listX, listY)
    meanXSquard = findMeanSquerd(listX)
    squerdMeanX = meanX * meanX
    return ((meanX * meanY) - meanXY) / (squerdMeanX - meanXSquard)


def findB(listX, listY):
    """":returns b"""
    meanX = findMean(listX)
    meanY = findMean(listY)
    m = findM(listX, listY)
    return meanY - (m * meanX)


def findRgrLine(listX, listY):
    """:returns regression line"""
    y = []
    for i in range(len(listX)):
        y.append((findM(listX, listY) * listX[i]) + findB(listX, listY))
    return y


def findy(x, listX, listY):
    """:returns the y of given x"""
    y = (findM(listX, listY) * x) + findB(listX, listY)
    return y


def xlist(data):
    """":returns list of x=1 -> x=n"""
    x = []
    t = 0
    while t < len(data):
        t += 1
        x.append(t)
    return x
