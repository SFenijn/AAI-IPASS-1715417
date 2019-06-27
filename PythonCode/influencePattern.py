import RandomDataGenerator as rgen
import linearRegression as lr
import clockFunctions as cl

def setbedtime_target():
    bt_target = float(input("Hoelaat wil je gaan slapen?"))
    return bt_target


def setwakuptime_target():
    wt_target = float(input("Hoelaat moet je uiterlijk opstaan?"))
    return wt_target


def setsleeptime_target():
    st_target = float(input("Hoelang wil je slapen?"))
    return st_target


def profile_setup(days):
    """"Make a list with the sleepdata and tagets on a set index position"""
    target_lst = []
    target_lst.append(setbedtime_target())
    target_lst.append(setwakuptime_target())
    target_lst.append(setsleeptime_target())

    sleepdata = rgen.generate_sleep_data(days)
    return target_lst, sleepdata


def update_profile(profile):
    bt = float(input("Waneer ben je gaan slapen?"))
    st = float(input("Hoelang heb je geslapen?"))
    profile[1][0].append(bt)
    profile[1][1].append(st)
    return profile


def auto_update_profile(profile, bt, st):
    profile[1][0].append(bt)
    profile[1][1].append(st)
    return profile


def difference(data, change, maxchange):
    """"returns te amount time to change"""
    bt_target = data[0][0]
    time_list = data[1][0][-6:]
    print(time_list)
    # make prediction for bedtime.
    predicted_bt = lr.findPrediction(lr.xlist(time_list)[-1] + 1, lr.xlist(time_list), time_list)

    # Calculate bedtime offset to bedtime target and restrict if need be
    diff = bt_target - predicted_bt
    bt_change = change * diff
    bt_change = abs(bt_change)
    if bt_change > maxchange:
        bt_change = maxchange
    return predicted_bt, bt_change, maxchange


def action_clock(diff, data):
    """"Returns the time when the action should take place"""
    target = cl.to_clock_strip_day(data[0][0])
    prediction = cl.to_clock_strip_day(diff[0])
    change = cl.to_clock_strip_day(diff[1])
    maxchange = diff[2]
    plus = prediction + change
    min = prediction - change
    print(plus)
    print(min)

    diff_p = abs(cl.clockToNum(plus) - cl.clockToNum(target))
    diff_m = abs(cl.clockToNum(min) - cl.clockToNum(target))
    print(diff_p)
    print(diff_m)

    if diff_p < diff_m:
        action_t = plus
    else:
        action_t = min
    # if action time is close to target just set the action time to the target time.
    target_ofset = abs(cl.clockToNum(action_t) - cl.clockToNum(target))
    if target_ofset <= cl.clockToNum(change)*3 and target_ofset <= maxchange:
        action_t = target

    return cl.clockToNum_with_day(action_t)


def action_numb(diff, data):
    """"Returns the number for the action"""
    target = data[0][0]
    prediction = diff[0]
    change = diff[1]
    maxchange = diff[2]
    plus = prediction + change
    min = prediction - change

    diff_p = abs(plus - target)
    diff_m = abs(min - target)

    if diff_p < diff_m:
        action_n = plus
    else:
        action_n = min
    # if action number is close to target set the action number to the target number.
    if abs(action_n - target) <= maxchange:
        action_n = target
    return action_n
