from PIL import Image

afbeelding = Image.open("minecraft.png")

afbeelding.show()

breedte = str(afbeelding.width)
hoogte = str(afbeelding.height)

helft_breedte = afbeelding.width // 2
helft_hoogte = afbeelding.height // 2

nieuwe_afmeting = (helft_breedte, helft_hoogte)

kleinere_afbeelding.save('minecraft_klein.png')


