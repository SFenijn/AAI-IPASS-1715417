import RandomDataGenerator as rgen
import linearRegression as lr
import clockFunctions as clk

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


def difference(data, change, maxchange):
    """"returns te time to change"""
    bt_target = data[0][0]

    # make prediction for bedtime.
    predicted_bt = lr.findPrediction(lr.xlist(data[1][0])[-1] + 1, lr.xlist(data[1][0]), data[1][0])

    # Calculate bedtime offset to bedtime target and restrict if need be
    diff = bt_target - predicted_bt
    bt_change = change * diff
    if bt_change > maxchange:
        bt_change = maxchange
    elif bt_change < -maxchange:
        bt_change = -maxchange
    return predicted_bt, bt_change


def actionTime(diff, data):
    print(diff)
    print(data)
    bt_target = data[0][0]
    predicted_bt = diff[0]
    bt_change = diff[1]

    action_time = predicted_bt + bt_change
    if action_time - bt_target <= bt_change and bt_target - action_time <= bt_change:
        action_time = bt_target
    return action_time


profile1 = profile_setup(14)
print(profile1)
change = difference(profile1, 0.2, 2)
bedtime = actionTime(change, profile1)

print(bedtime)
