import re

while True:

    invoer = input("voer je mobiele nummer in: ")

    patroon = r"^06-?\d{8}$"
    matches = re.findall(patroon, invoer)

    if(len(matches) > 0 ):
        break

print("nummer in juiste formaat:", matches[0])


while True:

    invoer2 = input("en vul hier je postcode in: ")

    patroon2 = r"^\d{4}[a-zA-Z]{2}$"
    matches2 = re.findall(patroon2, invoer2)

    if (len(matches2) > 0 ):
        break

print("postcode in juiste formaat:", matches2[0])


