from PIL import Image

afbeelding = Image.open("minecraft.png")

afbeelding.show()

breedte = afbeelding.width
hoogte = afbeelding.height

print("De afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")

print(afbeelding.format, afbeelding.size, afbeelding.mode)