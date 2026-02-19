import datetime
def get_time():
    time = datetime.datetime.now()
    ftime = time.strftime("%I:%M %p %b %d %Y")
    return ftime
