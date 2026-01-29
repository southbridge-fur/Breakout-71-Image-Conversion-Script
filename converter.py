#!/usr/bin/env python

import argparse
import colorsys
from colored import Fore, Back, Style, set_tty_aware
from PIL import Image, ImageOps

set_tty_aware()

parser = argparse.ArgumentParser(
    prog = "Breakout 71 image converter",
    description = "Converts an image to a custom stage string for the game Breakout 71. https://breakout.lecaro.me/",
    epilog = "Created by Southbridge. Licensed MIT. Available here https://github.com/southbridge-fur/Breakout-71-Image-Conversion-Script/"
)

parser.add_argument("filename")
parser.add_argument("-n","--name", help = "The name of the level to display in the level list. Defaults to the filename")
parser.add_argument("-c","--credit", help = "The credit to give for the image.")
parser.add_argument("--hsv", help="A comma-separated list of coefficients for hue, saturation, and value to use while finding the nearest color values.", type=str, default = "10.0,1.0,1.0")

MIN_SIZE = 6
MAX_SIZE = 21

TEMPLATE = """ 
```
[{name}]
{level}
[{credit}]
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
        int(color_str[0:2], 16),
        int(color_str[2:4], 16),
        int(color_str[4:6], 16)
    ])


COLOR_CODES = { key : Back.rgb(*rgb_string_to_tuple(key)) + Fore.white + value + Style.reset for key, value in COLOR_CODES.items() }

HSV_COLORS = {
    colorsys.rgb_to_hsv(*rgb_string_to_tuple(key)) : item
    for key,item in COLOR_CODES.items()
}

def find_nearest_color(pixel, hsv = (1.0, 1.0, 1.0)):
    if pixel is None:
        return None;
    hsv_color = colorsys.rgb_to_hsv(pixel[0], pixel[1], pixel[2])
    return min(HSV_COLORS.keys(), key=lambda x:
               abs(x[0]-hsv_color[0]) * float(hsv[0]) +
               abs(x[1]-hsv_color[1]) * float(hsv[1]) +
               abs(x[2]-hsv_color[2]) * float(hsv[2]))

def convert_image(filename, hsv):
    image = Image.open(filename)
    if image.size[0] > MAX_SIZE \
       or image.size[1] > MAX_SIZE:
        print("Image is too large {0}, must be smaller than {1} pixels on all sides.".format(image.size, MAX_SIZE))
        return ""

    largest_side = max(list(image.size) + [MIN_SIZE])
    padded_image = ImageOps.pad(image, (largest_side, largest_side), color=(0,0,0,0))

    image_string = ""
    
    for y in range(largest_side):
        for x in range(largest_side):
            pixel = padded_image.getpixel((x,y))
            if pixel[3] < 128: #alpha
                image_string += "_" 
                continue
            nearest = find_nearest_color(pixel, hsv)
            if nearest is None:
                image_string += "_" 
                continue
            image_string += HSV_COLORS[nearest]
        image_string += "\n"
    return image_string

if __name__ == "__main__":
    args = parser.parse_args()
    
    image_string = convert_image(args.filename, args.hsv.split(","))

    name = args.filename
    if not args.name is None:
        name = args.name

    credit = "No Credit"
    if not args.credit is None:
        credit = args.credit
        
    print (TEMPLATE.format(
        name = name,
        level = image_string,
        credit = credit))
    
              
