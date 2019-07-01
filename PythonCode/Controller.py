import linearRegression as lr
import clockFunctions as cl


def difference(data, change, maxchange):
    """"returns te amount time to change"""
    # receive data
    target = data[0][0]
    time_list = data[1][0][-6:]
    # make prediction for bedtime.
    predicted_bt = lr.findy(lr.xlist(time_list)[-1] + 1, lr.xlist(time_list), time_list)

    # Calculate bedtime offset to bedtime target.
    diff = target - predicted_bt
    bt_change = change * diff
    bt_change = abs(bt_change)

    # restrict to not go over the maxchange
    if bt_change > maxchange:
        bt_change = maxchange
    return predicted_bt, bt_change, maxchange


def action_clock(diff, data):
    """"Returns the time when the action should take place"""
    # receive data
    target = cl.to_clock_strip_day(data[0][0])
    prediction = cl.to_clock_strip_day(diff[0])
    prediction_with_day = cl.numToClock(diff[0])
    change = cl.to_clock_strip_day(diff[1])

    # check if the action needs to be later or earlier in the day.
    later = cl.closest(target, prediction, change)
    if later:
        return cl.clockToNum_with_day(prediction_with_day + change)
    else:
        return cl.clockToNum_with_day(prediction_with_day - change)


def integral(data):
    """"returns te amount time to change"""
    # set n for number of squars in riemann sum
    n = 100
    # receive data
    ylist = data[1][0]

    # calculate delta x, the 7 stands for the start of the PID influance
    deltax = len(ylist) - 0 / n

    #integral:
    i = 0
    intgrl = 0
    while i < len(ylist[7:]):
        # get y
        y = lr.findy(i, lr.xlist(ylist[7:]), ylist[7:]) - ylist[6]
        # calculate integral
        area = y *deltax
        intgrl += area

        i += deltax
    return intgrl


def pid(setpoint, ylist, previous_e, integral, Kp, Ki, Kd):
    """"PID controller to smoothly go to target(setpoint)"""
    # get measured value
    measured_value = lr.findy(lr.xlist(ylist)[-1] + 1, lr.xlist(ylist), ylist)
    # reset previous error
    previous_error = previous_e
    error = abs(setpoint - measured_value)
    # set newintegral
    newintegral = integral + error
    # I and D
    integral = (integral + error) / 0.1
    derivative = (error - previous_error) / 0.1
    # output and tuning
    output = (Kp * error) + (Ki * integral) + (Kd * derivative)
    return output, measured_value, error, newintegral


def action_clock2(diff, measured_value, data):
    """"Returns the time when the action should take place"""
    # receive data
    target = cl.to_clock_strip_day(data[0][0])
    prediction = cl.to_clock_strip_day(measured_value)
    prediction_with_day = cl.numToClock(measured_value)
    change = cl.to_clock_strip_day(diff)

    # check if the action needs to be later or earlier in the day.
    later = cl.closest(target, prediction, change)
    if later:
        return cl.clockToNum_with_day(prediction_with_day + change)
    else:
        return cl.clockToNum_with_day(prediction_with_day - change)


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