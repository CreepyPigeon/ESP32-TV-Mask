from PIL import Image
import numpy as np

#img = Image.open('heart.png')
#ary = np.array(img)

#r,g,b = np.split(ary,3,axis=2)
#r=r.reshape(13, 17)
#g=r.reshape(13, 17)
#b=r.reshape(13, 17)

#print(r)
#print(g)
#print(b)

img = Image.open('./images/eye.png')
pixels = list(img.getdata())
#print(pixels)
reversed_pixels = pixels[::-1]


def transform_to_crgb(data):
    transformed_data = ", ".join([f"CRGB({r}, {g}, {b})" for r, g, b in data])
    return transformed_data

crgb_data = transform_to_crgb(reversed_pixels)
print(crgb_data)