#!/usr/bin/python3

from fileinput import input

print("Hi! What's your name?")
name = input().readline().strip()

print()
print("You ask if I can count?! Don't be silly, %s ... I am a COMPUTER!" % name)

print()

for n in range(10):
	print(n + 1)
