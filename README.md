# Image Conversion Script for Breakout 71

This is a simple image conversion script for the game Breakout 71 that converts an image into a custom level.

The game can be found here https://breakout.lecaro.me/

I am not affiliated with the creator and just made this script because I was feeling burned out on an idle Thrusday. 

### Usage

```bash
$ python converter.py --help
usage: Breakout 71 image converter [-h] [-n NAME] [-c CREDIT] [--hsv HSV] filename

Converts an image to a custom stage string for the game Breakout 71. https://breakout.lecaro.me/

positional arguments:
  filename

options:
  -h, --help           show this help message and exit
  -n, --name NAME      The name of the level to display in the level list. Defaults to the filename
  -c, --credit CREDIT  The credit to give for the image.
  --hsv HSV            A comma-separated list of coefficients for hue, saturation, and value to use while finding the nearest color values.
```