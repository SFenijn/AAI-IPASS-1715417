import matplotlib.pyplot as plt
import numpy as np
import linearRegression as lr
import clockFunctions as cl


def drawgrapth(profile, altered_profile):
    """"draw graph"""
    # make x tiks
    x = lr.xlist(altered_profile[1][0])

    # make y tiks
    altered_data = altered_profile[1][0]
    random_data = cl.lst_strip_day(profile[1][0])

    # make Ys ready for graph
    altered_data = cl.lst_strip_day(altered_data)
    random_data = cl.lst_strip_day(random_data)

    # draw graph
    plt.plot(x, altered_data)
    plt.plot(x, random_data, 'ro')
    plt.yticks(np.arange(0, 24, step=1))
    plt.xticks(np.arange(0, 61, step=7))
    plt.show()
