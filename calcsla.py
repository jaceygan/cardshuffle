from dateutil.relativedelta import relativedelta
# constant
SECINYEAR = 31536000


def downtime(sla):
    yeardowntime = (1-(sla*0.01)) * SECINYEAR

    results = {}
    results["Yearly Downtime"] = pretty(yeardowntime)
    results["Monthly Downtime"] = pretty(yeardowntime/12)
    results["Weekly Downtime"] = pretty(yeardowntime/52)
    results["Daily Downtime"] = pretty(yeardowntime/365)

    return results

def pretty(t):
    units = ['days', 'hours', 'minutes', 'seconds']
    human_readable = lambda delta: ['%d%s' % (getattr(delta, unit), unit if getattr(delta, unit) > 1 else unit[:-1]) 
        for unit in units if getattr(delta, unit)]

    s = ""
    for ea in human_readable (relativedelta(seconds=t)):
        s+= ea+" "

    return s[:-1]
   
print(downtime(99.7))