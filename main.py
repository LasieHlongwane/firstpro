# Python password generator

import random

passLength = int(input("Enter the desired length for your Password: "))
passGenerated = int(input("How many passwords would you like to generate? "))

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*()_=;.,<>?/`~+-"

upper, lower, nums, syms = True, True, True, True

all_Characters = ""

if upper:
    all_Characters += uppercase_letters
if lower:
    all_Characters += lowercase_letters
if nums:
    all_Characters += digits
if syms:
    all_Characters += symbols

for x in range(passGenerated):
    password = "".join(random.sample(all_Characters, passLength))
    print(password)
