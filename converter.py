import os
import sys
import colorsys
from PIL import Image, ImageOps

MIN_SIZE = 6
MAX_SIZE = 21

TEMPLATE = """ 
```
[{name}]
{level}
[{credits}]
```
"""

COLOR_CODES = {
    # "#000000" : "B", # Bombs
    "#000000" : "g", # convert black to grey instead
    "#FFFFFF" : "W",
    "#231F20" : "g",
    "#FFD300" : "y",
    "#6262EA" : "b",
    "#5DA3EA" : "t",
    "#E67070" : "s",
    "#E32119" : "r",
    "#AB0C0C" : "R",
    "#59EEA3" : "c",
    "#A1F051" : "G",
    "#A664E8" : "v",
    "#E869E8" : "p",
    "#5BECEC" : "a",
    "#53EE53" : "C",
    "#F44848" : "S",
    "#E66BA8" : "P",
    "#F29E4A" : "O",
    "#618227" : "k",
    "#E1C8B4" : "e",
    "#9B9FA4" : "l"
}

def rgb_string_to_tuple(color_str):
    if color_str.startswith("#"):
        color_str = color_str[1:]
    return tuple([
        int(color_str[0:1], 16),
        int(color_str[2:3], 16),
        int(color_str[4:5], 16)
    ])

HSV_COLORS = {
    colorsys.rgb_to_hsv(*rgb_string_to_tuple(key)) : item
    for key,item in COLOR_CODES.items()
}

def find_nearest_color(pixel):
    if pixel is None:
        return None;
    hsv_color = colorsys.rgb_to_hsv(pixel[0], pixel[1], pixel[2])
    return min(HSV_COLORS.keys(), key=lambda x:
               abs(x[0]-hsv_color[0]) * 10 + # We want to prioritize matching hues over saturation and value.
               abs(x[1]-hsv_color[1]) +
               abs(x[2]-hsv_color[2]))
        
for infile in sys.argv[1:]:
    image = Image.open(infile)
    if image.size[0] > MAX_SIZE \
       or image.size[0] < MIN_SIZE \
       or image.size[1] > MAX_SIZE \
       or image.size[1] < MIN_SIZE:
        print("Image is the wrong size {0}".format(image.size))
        continue

    largest_side = max(image.size)
    padded_image = ImageOps.pad(image, (largest_side, largest_side), color=(0,0,0,0))

    image_string = ""
    
    for y in range(largest_side):
        for x in range(largest_side):
            pixel = padded_image.getpixel((x,y))
            if pixel[3] < 128: #alpha
                image_string += "_" 
                continue
            nearest = find_nearest_color(pixel)
            if nearest is None:
                image_string += "w" 
                continue
            image_string += HSV_COLORS[nearest]
        image_string += "\n"
    print(TEMPLATE.format(name = infile, level = image_string, credits="bweh"))

              
