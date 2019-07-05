import random


def generate_base_line(seed):
    """"Generates basses for bed-time, and sleep-time"""
    random.seed(seed)
    bed_time = random.randint(0, 24)
    sleep_time = random.randint(3, 13)
    return bed_time, sleep_time


def generate_sleep_data(len, seed):
    """"generates random sleepdata with the use of a seed"""
    base = generate_base_line(seed)
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


def generate_error_data(len, seed):
    """"generates random errors with the use of a seed"""
    random.seed(seed)
    error = 0
    error_lst = []
    for i in range(len):
        error = round(random.uniform(-1.0, 1.0), 3)
        error_lst.append(error)
    return error_lst


def generate_diviation_from_target(len, seed):
    """"generates random errors with the use of a seed"""
    random.seed(seed)
    error = 0
    error_lst = []
    for i in range(len):
        error = error + round(random.uniform(-1.0, 1.0), 3)
        error_lst.append(error)
    return error_lst


def get_wakeup_time(data):
    """calculates wakeuptimes based on bedtime and sleeptime"""
    wakeup_time_lst = []
    for i in range(len(data[1])):
        wakeup_time = data[0][i] + data[1][i]
        wakeup_time_lst.append(wakeup_time)
    return wakeup_time_lst


def procentage_bool(percentage):
    """":returns boolean based on given %"""
    chance = percentage / 100
    rand = random.random()
    return chance > rand


def generate_error(value):
    """"takes a value and gives it an error"""
    return value + round(random.uniform(-3.0, 3.0), 3)

