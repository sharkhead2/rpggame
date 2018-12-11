import random
import time
import dictionary as d
import math
from os import system, name
import WeaponExtras as we
import ArmorExtras as ae
import termios, fcntl, sys, os


def rounddown(x):
    return int(math.floor(x / 10.0)) * 10

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def print_loot(loot):
    if loot.gear == 'weapon':
        we.weaponprint(loot)
    elif loot.gear in ['helmet', 'arms', 'chest', 'leggings', 'boots']:
        ae.armorprint(loot)

def takeallinput():
    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    try:
        while 1:
            try:
                c = sys.stdin.read(1)
            except IOError:
                return None
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
