import re

while True:

    invoer = input("voer je mobiele nummer in: ")

    patroon = r"^06-?\d{8}$"
    matches = re.findall(patroon, invoer)

    if(len(matches) > 0 ):
        break

print("bedankt nummer in juiste formaat:", matches[0])