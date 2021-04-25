
#Import required Image library
import os
from PIL import Image, ImageDraw, ImageFont

#Create an Image Object from an Image
im = Image.open(os.path.join("E:\python-basics\week-4\images", "test.jpeg"))
width, height = im.size

draw = ImageDraw.Draw(im)
text = "Aman Zishan"

font = ImageFont.truetype('arial.ttf', 36)
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 30
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)
im.show()

#Save watermarked image
im.save(os.path.join("E:\python-basics\week-4\images", "watermark.jpeg"))