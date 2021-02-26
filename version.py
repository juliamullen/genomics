import datetime

def get_release(self):
    return datetime.datetime.now().strftime('%Y-%m-%d-%H:%M')
