'''Custom Seating Cards'''

import os
from PIL import Image, ImageDraw, ImageFont
"""crop flower image
flower = Image.open('flower.jpg')
flower2 = flower.resize((int(width / 4), int(height / 2)))
flower2.save('cropFlower.png')
flower2.show()
flower2.save('cropFlower.jpg')"""

card = Image.new('RGBA', (360, 288), 'white')
flower = Image.open('cropFlower.jpg')
flowerCopy = flower.copy()
card.paste(flowerCopy, (0,110))
card2 = Image.new('RGBA', (364, 392), 'black')
card2.paste(card, (2,2))
card2.save('card2.png')

def creating_card(guestsnames):
    ceatingCard = Image.open('card2.png')
    font = ImageFont.truetype('coolvetica rg.ttf', 15)
    draw = ImageDraw.Draw(ceatingCard)
    draw.text((120, 100), guestsnames, fill = 'blue', font = font)
    ceatingCard.save(guestsnames + '.png')


with open('guests.txt') as g:
    guests = g.readlines()

for guest in guests:
    creating_card(guest)
