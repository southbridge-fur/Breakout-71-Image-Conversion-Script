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

---

To run the script fully from nothing:

```bash
$ git clone https://github.com/southbridge-fur/Breakout-71-Image-Conversion-Script.git b71
$ cd b71
$ python -m venv venv
$ source venv/bin/activate
$ python -m pip install -r requirements.txt
$ python convert.py 
```

### Example

```bash
$ python converter.py ../kirby.png --name "Kirby" --hsv "6.0,1.0,0.1"
```

```
[Kirby]
__ggg_gggggg_gg_
_gPWPgPWWWWPgPPg
gPWWWPWWWWWWPgWg
gWWWWWWWWWWWWPWg
gPWWWWWWWgWgWWWg
_gPWWWWWWgWgWWPg
_ggPWWWWWgWgWWg_
_gPWWWPPWWWWWPg_
_gPWWWWWWWWWWWg_
__gWWWWWWWgWWPg_
__gPWWWWWWWWWg__
_gPgPWWWWWWWPg__
_gPPggPWWWPPg___
_gPPPggggggg____
_gPPg_gPPg______
__gg___gg_______

[No Credit]
```