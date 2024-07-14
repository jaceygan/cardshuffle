from dateutil.relativedelta import relativedelta
# constant
SECINYEAR = 31536000
SECINMIN = 60
SECINHOUR = 3600
SECINDAY = 86400

def downtime(sla):
    #everything is in seconds
    yeardowntime = (1-(sla*0.01)) * SECINYEAR
    monthdowntime = yeardowntime/12
    weekdowntime = yeardowntime/52
    daydowntime = weekdowntime/7

    return [pretty(yeardowntime), pretty(monthdowntime), pretty(weekdowntime), pretty(daydowntime)]

def pretty(t):
    attrs = ['years', 'months', 'days', 'hours', 'minutes', 'seconds']
    human_readable = lambda delta: ['%d %s' % (getattr(delta, attr), attr if getattr(delta, attr) > 1 else attr[:-1]) 
        for attr in attrs if getattr(delta, attr)]

    return(human_readable (relativedelta(seconds=t)))


print(downtime(99.7))