# constant
SECINYEAR = 31536000



def downtime(sla):
    yeardowntime = (100.0-sla) * SECINYEAR
    monthdowntime = yeardowntime/12
    weekdowntime = yeardowntime/52
    daydowntime = weekdowntime/7

    return [pretty(yeardowntime), pretty(monthdowntime), pretty(weekdowntime), pretty(daydowntime)]

def pretty(t): # work on this
    return None

def convertToMin(sec):
    if sec>60:
        return (sec/60.0)

def convertToHour(min):
    if min>60:
        return (min/60.0)

def convertToDay(hour):
    if hour>24:
        return (hour/24.0)

