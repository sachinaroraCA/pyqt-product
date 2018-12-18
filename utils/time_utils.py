import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    if type(dt) == str:
        dt = datetime.datetime.strptime(dt.strip("'"), '%Y-%m-%d %H:%M')
    return (dt - epoch).total_seconds() * 1000


def get_current_time():
    current_time = unix_time_millis(datetime.datetime.now())
    return int(current_time)
