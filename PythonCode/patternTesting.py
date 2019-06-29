import influencePattern as ip


def use_profile(profile):
    """"takes a profile and splits it in data to use for pattern influence"""
    use_data = [profile[1][0][0:7], profile[1][1][0:7]]
    return profile[0], use_data


def simulate_usecase(profile, change, maxchange, loops):
    maxloops = loops - 7
    count = 0
    while count < maxloops:
        diff = ip.difference(profile, change, maxchange)
        action_t = ip.action_clock(diff, profile)
        profile[1][0].append(action_t)

        count += 1
    return profile
