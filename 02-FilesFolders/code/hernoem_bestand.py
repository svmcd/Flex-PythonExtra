import os 

bestandsnaam = "demobestand"

huidige_map = os.getcwd()

volledige_pad = os.path.join(huidige_map, bestandsnaam)
print("dit bestand gaan we hernoemen: " + volledige_pad)

# Om nieuwe naam vragen
nieuwe_naam = input("Nieuwe bestandsnaam: ")

if len(nieuwe_naam) > 0:
    # Map en nieuwe bestandsnaam gebruiken om volledige pad samen te stellen
    nieuwe_volledige_pad = os.path.join(huidige_map, nieuwe_naam)
    print("Bestand wordt hernoemd naar: " + nieuwe_volledige_pad)

    # Bestand hernoemen 
    os.rename(volledige_pad, nieuwe_volledige_pad)
    print("Bestand hernoemd")
else:
    print("Sorry, geen geldige invoer, einde programma")