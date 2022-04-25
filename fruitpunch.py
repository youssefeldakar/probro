#!/usr/bin/python3

import sys

from fileinput import input
from random import *

print("Tell me the names of 5 fruits that you like!")

items = input().readline().split()

if (len(items) < 5):
    print("Wrong! You gave me less than 5 fruits!")
    sys.exit(1)

if (len(items) > 5):
    print("Wrong! You gave me more than 5 fruits!")
    sys.exit(1)

print("I would like to pick 3 items and give you a fruitpunch...")

picks = []

for n in range(3):
    while True:
        pick = choice(items)

        if picks.count(pick) == 0:
            picks.append(pick)
            print(pick)
            break
        else:
            print("Whoops, let me try again, I've already picked this one: " + pick)
