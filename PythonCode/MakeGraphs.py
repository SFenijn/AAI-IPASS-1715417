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
    plt.plot(x, altered_data, label="altered times")
    plt.plot(x, random_data, 'ro', label="unaltered times")
    plt.yticks(np.arange(0, 24, step=1))
    plt.xticks(np.arange(0, 61, step=7))
    # make labels
    plt.xlabel("Time in days")
    plt.ylabel("time of day")
    plt.legend(loc='upper left')
    plt.show()


def draw_pid_grapth(target, pid_data, errors, error_dict):
    """"draw graph"""
    # make x tiks
    x = lr.xlist(pid_data)

    # draw graph
    plt.plot(x, pid_data, label="with PID")
    plt.plot(x, errors, label="no PID")
    plt.axhline(y=target, linewidth=1, color='k')
    plt.scatter(list(error_dict.keys()), list(error_dict.values()), color='black')

    # make labels
    plt.xlabel("Time in days")
    plt.ylabel("diviation from target")
    plt.legend(loc='upper left')
    plt.show()
