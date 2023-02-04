from get_text import get_text
from send_req_ import tweet
from time import time

def nextTime():
    interval = int(open("interval.txt", "r").read())
    lastTime = int(open("nextTime.txt", "r").read())

    nextTime = lastTime + interval

    open("nextTime.txt", "w").write(str(nextTime))

while True:
    if time()-int(open("nextTime.txt", "r").read()) < 16.1:
        tweet(get_text())
        nextTime()