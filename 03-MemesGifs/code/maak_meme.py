from PIL import Image, ImageFont, ImageDraw

afbeelding = Image.open("meme_background.png")

afbeelding.show()

breedte = afbeelding.width
hoogte = afbeelding.height

print("De afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")

print(afbeelding.format, afbeelding.size, afbeelding.mode)

lettertype = ImageFont.truetype("impact.ttf", 50)

tekengebied = ImageDraw.Draw(afbeelding)

tekst = "Coding in Python\nNo problemo!"

tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype)

tekst_x = (breedte - tekst_breedte) / 2
tekst_y = (breedte - tekst_hoogte) / 2

print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))

tekengebied.multiline_text((tekst_x, tekst_y), tekst, font=lettertype, fill=(0,0,0))

tekengebied.multiline_text((tekst_x-2, tekst_y-2), tekst, font=lettertype, fill=(255,255,255))

afbeelding.show()

afbeelding.save("meme_met_tekst.png")

