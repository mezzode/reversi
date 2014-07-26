import pygame
pygame.init()
import os.path

# if os.path.isfile('')
# if config file doesnt exist:
import configparser
if not os.path.isfile('config.ini'):
    config = configparser.ConfigParser()
    # config['DEFAULT'] = {} # default values for each section here
    config['colours'] = {}
    colours = config['colours']
    colours['dark'] = '0,0,0'
    colours['light'] = '230,230,230'
    colours['space_colour'] = '153, 204, 153'
    colours['help_colour']  = '100,200,100'
    colours['panel_colour'] = '253,253,253'
    colours['highlight_colour'] = '240,240,240'
    config['window'] = {}
    window = config['window']
    window['fullscreen'] = 'False'
    window['width'] = '1280'
    window['height'] = '800'
    with open('config.ini','w') as configfile: # save to config.ini
        config.write(configfile)

def colourCheck(colour,defaultColour):
    if isinstance(colour,str):
        try:
            r,g,b = colour.split(',')
            r = int(r)
            g = int(g)
            b = int(b)
            if r > 255 or g > 255 or b > 255:
                colour = defaultColour
            else:
                colour = r,g,b
        except ValueError:
            colour = defaultColour
    elif isinstance(colour,tuple):
        colour = colour
    else:
        colour = defaultColour
    return colour

# Colours
black = 0,0,0
white = 255,255,255
red = 255,100,100
purple = 255,0,255
blue = 0,0,100
yellow = 200,200,0

# Defaults
dark  = 0,0,0                  # black
light = 230, 230, 230          # light grey
panel_colour = 253,253,253     # off white
space_colour = 153, 204, 153   # light green
helpGreen = 100,200,100        # brighter green
highlight_colour = 240,240,240 # lighter grey

dark_defaults = {'black':black, 'red':red, 'purple':purple}
light_defaults = {'white':white, 'blue':blue, 'yellow':yellow}

config = configparser.ConfigParser()
config.read('config.ini')

colours = config['colours']
dark  = colourCheck(colours.get('dark'),dark)
light = colourCheck(colours.get('light'),light)
space_colour = colourCheck(colours.get('space_colour'),space_colour)
helpGreen = colourCheck(colours.get('help_colour'),helpGreen)
panel_colour = colourCheck(colours.get('panel_colour'),panel_colour)
highlight_colour = colourCheck(colours.get('highlight_colour'),highlight_colour)

window = config['window']
width = int(window['width'])
height = int(window['height'])
size = width, height # screen size

# Fonts
font_small = pygame.font.Font("Quicksand-Light.ttf", 44)
font_med = pygame.font.Font("Quicksand-Light.ttf", 48)