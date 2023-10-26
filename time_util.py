from time import sleep
from random import randint

def sleep_for_sec(seconds):
    sleep(seconds)


def sleep_for_rand_between(start, end):
    sleep(randint(start, end))
