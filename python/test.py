from PIL import Image,ImageDraw,ImageFont
import os

#print(os.listdir("movie"))

url = "/Users/moonmisty/PycharmProjects/5/{}"
color = ["red","blue","yellow"]

def draw(url,saved_url):
    image = Image.open(url)
    xSize,ySize =Image.size
    fontSize = int(ySize/4)

    position = xSize-2*fontSize
    myFont = ImageFont.truetype("Arial.ttf",fontSize)
    ImageDraw.Draw(image).text((position,0),"hello",font=myFont,fill=color)
    image.save("trash/"+saved_url)

for i in os.listdir("moive"):
    if ".jpg" in i:
        draw(url.format(i),"saved_"+i)
