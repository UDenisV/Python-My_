class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

def after(a, b):
    if a.hours > b.hours:
        return True
    elif a.hours == b.hours:
        if a.minutes > b.minutes:
            return True
        elif a.minutes == b.minutes:
            if a.minutes > b.minutes:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
