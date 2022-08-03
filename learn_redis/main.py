from random import randint
from time import sleep
import redis

r = redis.Redis()


def get_channel():
    channels = ["football-1", "football-2"]
    return channels[randint(0, 1)]


for _ in range(10):
    ch = get_channel()
    print(ch)
    r.publish(ch, "Messi scored")
    sleep(2)
