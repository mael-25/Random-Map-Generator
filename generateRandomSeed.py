import datetime
import time

import pytz

def getSeed(seed, seed_of_the_day):
    if seed_of_the_day == True:
        return seedOfTheDay()
    if seed == -1: 
        tim = datetime.datetime.now()
        randseed = tim.month*3600000*31*24+tim.day*3600000*24+tim.hour*3600000+tim.minute*60000+tim.second*1000+tim.microsecond
        return randseed
    return seed 

def seedOfTheDay():
    # timezone = datetime.timezone()
    tim = datetime.datetime.now(tz=pytz.timezone("Greenwich"))
    seed = tim.year*12*31+tim.month*31+tim.day
    tim.today()
    return seed