import RandomDataGenerator as rn
import Controller as con
import MakeGraphs as graph

print(rn.generate_error_data(12345, 59))


def PID_loop(error_data, target, maxloops , Kp, Ki, Kd, percentage):
    """function ajust a value with a PID controller"""
    adjustment_values = []
    ylist = []
    error_dict = {}
    current_value = 0
    count = 0
    error = 0
    integral = 0

    while count < maxloops:
        pid = con.pid_no_regression(target, current_value, error, integral, Kp, Ki, Kd)
        adjustment_values.append(pid[0])
        error = pid[1]
        integral = pid[2]

        # adjust current_value and add to list
        current_value += pid[0]
        if rn.procentage_bool(percentage):
            current_value += error_data[count]
            e = {count + 1: error_data[count]}
            error_dict.update(e)
        ylist.append(current_value)
        count += 1
    return ylist, error_dict


seed = 12345
target = 3
day_count = 100
percentage = 100
errors = rn.generate_error_data(day_count, seed)
afwijking = rn.generate_diviation_from_target(day_count, seed)
pid_information = PID_loop(errors, target, day_count, 0.1, 0.000030, 0.015, percentage)
pid_ylist = pid_information[0]
error_dict = pid_information[1]
graph.draw_pid_grapth(target, pid_ylist, afwijking, error_dict)

