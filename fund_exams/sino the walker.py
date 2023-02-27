def convert_time_into_seconds(time):
    return int(time[0]) * 60 * 60 + int(time[1]) * 60 + int(time[2])


def convert_to_hours(current_time):
    hours = current_time // 3600
    minutes = (current_time % 3600) // 60
    seconds = (current_time % 3600) % 60
    return f"Time Arrival: {hours:02d}:{minutes:02d}:{seconds:02d}"


leaving_time = input().split(":")
number_steps = int(input())
seconds_for_step = int(input())
time_seconds = convert_time_into_seconds(leaving_time)
time_seconds += number_steps * seconds_for_step
time = time_seconds % 86400
print(convert_to_hours(time))
