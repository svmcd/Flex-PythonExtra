import re

emails = []

with open("dummy.txt", "r") as bestand:

    regel = bestand.readline()

    while regel:

        patroon = r"..." # juiste regular expression voor email hier invullen

        gevonden = re.findall(...) # juiste code hier invullen

        ... # alle gevonden emails aan de email list toevoegen

        regel = bestand.readline() # volgende regel lezen

print(emails)