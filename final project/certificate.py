from PIL import Image, ImageDraw, ImageFont
import pandas as pd

df = pd.read_csv('list.csv')
font = ImageFont.truetype('arial.ttf',60)
font1 = ImageFont.truetype('arial.ttf',50)
for index,j in df.iterrows():
    img = Image.open('certificate.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(725,760),text='{}'.format(j['name']),fill=(115,240,123),font=font)
    draw.text(xy=(250,800),text='Aman Zishan',fill=(0,0,0),font=font1)
    img.save('pictures/{}.jpg'.format(j['name'])) 