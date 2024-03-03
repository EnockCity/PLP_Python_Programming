#!/usr/bin/python3
'''This program prompts the user to enter his/her
name,age and location and then prints
a personalized message using his/her details.'''

name = input("What's your name?")

age = int(input("What's your age?"))

location = input("Where do you live?")

print(f"Hello {name},you are {age} years old and live in {location}.")
