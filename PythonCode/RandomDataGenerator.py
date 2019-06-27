import random
import random as r


def generate_base_line():
    """"Generates basses for bed-time, and sleep-time"""
    bed_time = r.randint(0, 24)
    sleep_time = r.randint(3, 13)
    return bed_time, sleep_time


def generate_sleep_data(len):
    base = generate_base_line()
    bed_time = base[0]
    bed_time_lst = []
    sleep_time_lst = []
    for i in range(len):
        bed_time = bed_time + round(random.uniform(-1.0, 1.0), 3)
        bed_time_lst.append(bed_time)

        if base[1] <= 5:
            sleep_time = base[1] + round(random.uniform(0.0, 1.0), 3)
        elif base[1] <= 8:
            sleep_time = base[1] + round(random.uniform(-1.0, 1.0), 3)
        else:
            sleep_time = base[1] + round(random.uniform(-.0, 0.0), 3)
        sleep_time_lst.append(sleep_time)
    return bed_time_lst, sleep_time_lst

def get_wakeup_time(data):
    wakeup_time_lst = []
    for i in range(len(data[1])):
        wakeup_time = data[0][i] + data[1][i]
        wakeup_time_lst.append(wakeup_time)
    return wakeup_time_lst

