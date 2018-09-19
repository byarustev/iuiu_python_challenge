import datetime


def get_time():
    time_now = datetime.datetime.now()
    day_name = time_now.strftime("%A")
    hour_label = time_now.strftime("%I %p")
    minutes_seconds = time_now.strftime("%M:%S")
    to_print_string = "Today is :"+day_name+" Time is "+hour_label+" :"+minutes_seconds
    return to_print_string


print(get_time())
