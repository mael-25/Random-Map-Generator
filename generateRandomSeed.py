import datetime

def getSeed(seed):
    if seed == -1: 
        tim = datetime.datetime.now()
        randseed = tim.hour*3600000+tim.minute*60000+tim.second*1000+tim.microsecond
        return randseed
    return seed 