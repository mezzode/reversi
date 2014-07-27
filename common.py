import pygame
pygame.init()
import configparser
import os.path

if not os.path.isfile('config.ini'):
    # config.ini does not exist, must create one

    config = configparser.ConfigParser()
    # config['DEFAULT'] = {} # default values for each section here
    config['colours'] = {}
    colours = config['colours']
    colours['dark'] = '0,0,0'
    colours['light'] = '230,230,230'
    colours['space_colour'] = '153,204,153'
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
try:
    fullscreen = window.getboolean('fullscreen')
except ValueError:
    fullscreen = False
info = pygame.display.Info()
if fullscreen:
    width = info.current_w
    height = info.current_h
else:
    try:
        width = int(window['width'])
        if width > info.current_w:
            width = 1280
    except ValueError:
        width = 1280
    try:
        height = int(window['height'])
        if height > info.current_h:
            height = 800
    except ValueError:
        height = 800
size = width, height # screen size

# Fonts
font_small = pygame.font.Font("Quicksand-Light.ttf", 44)
font_med = pygame.font.Font("Quicksand-Light.ttf", 48)
font_large = pygame.font.Font("Quicksand-Light.ttf", 72)
font_title = pygame.font.Font("Quicksand-Light.ttf", 100)

controls_width = 360
controls_buffer = 20
panel_width = (controls_width-20)/2
panel_height = 100
space_buffer = 10
side = 70
board_width = board_height = (side * 8) + (space_buffer * 7)
full_width = board_width + controls_buffer + controls_width
full_height = board_height
x_buffer = (width - full_width)/2
y_buffer = (height - full_height)/2

# Spaces (i.e. Board)
space_sides  = side, side  # Size of each space i.e. 70 px by 70 px
space = pygame.Surface(space_sides)
space.fill(space_colour)
spaces = [[0 for x in range(8)] for x in range(8)] # Spaces Array (i.e. Board) init
for x in range(8):
    for y in range(8):
        spaces[x][y] = pygame.Rect((x_buffer + (side + space_buffer) * x, y_buffer + (side + space_buffer) * y),space_sides)

# P1's and P2's Counters
counter1 = pygame.Surface(space_sides)
counter1.fill(dark)
counter2 = pygame.Surface(space_sides)
counter2.fill(light)

# Help-highlighted Spaces
help_counter = pygame.Surface(space_sides)
help_counter.fill(helpGreen)
space_help = [[0 for x in range(8)] for x in range(8)]