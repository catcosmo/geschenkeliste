# BETRIEBSANLEITUNG ADVENTSKALENDER 2017

import datetime

wg = {
    0: 'cat',
    1: 'caro',
    2: 'jule',
    3: 'julz',
    4: 'hein',
    5: 'manou',
    6: 'maxx',
    7: 'peter'
}

now = datetime.datetime.now()

jackpot = now.day % 8

print 'adventskalenderpluendererin des tages ist ' + wg[jackpot] + '!'

# HOHOHO!