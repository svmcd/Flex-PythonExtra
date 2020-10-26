import re

emails = []

with open("/Users/samed/Documents/Mediacollege/Bewijzenmap/Jaar 1/periode 1/Flex lessen/Flex-PythonExtra/04-Tekst/code/emailsTekst.txt", "r") as bestand:

    regel = bestand.readline()

    while regel:

        patroon = r"[^@]+@[^@]+\.[^@]+"

        gevondenEmails = re.findall(patroon, regel)

        emails.extend(gevondenEmails)

        regel = bestand.readline() 

print(emails)