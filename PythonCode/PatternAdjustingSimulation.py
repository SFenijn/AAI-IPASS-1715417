import Controller as con


def simulate_proportional(profile, change, maxchange, loops, measure_days):
    """function to simulate adjusting a pattern with a proportional controller"""
    maxloops = loops - measure_days
    count = 0
    while count < maxloops:
        diff = con.difference(profile, change, maxchange)
        action_t = con.action_clock(diff, profile)
        profile[1][0].append(action_t)

        count += 1
    return profile


def simulate_pid(profile, loops, measure_days):
    """function to simulate adjusting a pattern with a PID controller"""
    pid_tuning = [0.3, 0.0055, 0.0015]
    setpoint = profile[0][0]
    starttime = profile[1][0][-1]

    maxloops = loops - measure_days
    count = 0
    error = 0
    integral = 0
    while count < maxloops:
        pid = con.pid(setpoint, profile[1][0], error, integral, pid_tuning[0], pid_tuning[1], pid_tuning[2])
        profile[1][0].append(pid[0])
        error = pid[2]
        integral = pid[3]
        count += 1
    return profile
