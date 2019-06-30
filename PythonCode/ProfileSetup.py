import RandomDataGenerator as rgen


def setbedtime_target():
    """":returns target"""
    bt_target = float(input("Hoelaat wil je gaan slapen?"))
    return bt_target


def setwakuptime_target():
    """":returns target"""
    wt_target = float(input("Hoelaat moet je uiterlijk opstaan?"))
    return wt_target


def setsleeptime_target():
    """function to set the amound of time you want to sleep"""
    st_target = float(input("Hoelang wil je slapen?"))
    return st_target


def profile_setup(days, seed):
    """"Make a list with the sleepdata and tagets on a set index position"""
    target_lst = []
    target_lst.append(setbedtime_target())

    sleepdata = rgen.generate_sleep_data(days, seed)
    return target_lst, sleepdata


def update_profile(profile):
    """"Function to update profile for GUI"""
    bt = float(input("Waneer ben je gaan slapen?"))
    st = float(input("Hoelang heb je geslapen?"))
    profile[1][0].append(bt)
    profile[1][1].append(st)
    return profile


def auto_update_profile(profile, setpoint):
    """"function to update profile without GUI"""
    profile[1][0].append(setpoint)
    return profile


def use_profile(profile, days):
    """"takes a profile and splits it in data to use for pattern influence"""
    use_data = [profile[1][0][0:days], profile[1][1][0:days]]
    return profile[0], use_data
