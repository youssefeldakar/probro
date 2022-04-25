#!/usr/bin/python3

from fileinput import input

my_input = input()

print("Enter first name:")
first_name = my_input.readline().strip()

print("Enter middle name:")
middle_name = my_input.readline().strip()

print("Enter last name:")
last_name = my_input.readline().strip()

print("Full name: %s %s %s" % (first_name, middle_name, last_name))
