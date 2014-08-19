import pygame
pygame.init()
import configparser
import os.path

if not os.path.isfile('config.ini'):
    # if config.ini does not exist, create one
    config = configparser.ConfigParser()
    config['colours'] = {}
    colours = config['colours']
    colours['dark (P1)'] = '0, 0, 0'
    colours['light (P2)'] = '230, 230, 230'
    colours['board'] = '153, 204, 153'
    colours['panels'] = '253, 253, 253'
    config['window'] = {}
    window = config['window']
    window['fullscreen'] = 'False'
    window['width'] = '1280'
    window['height'] = '800'
    with open('config.ini','w') as configfile: 
        # save to config.ini
        config.write(configfile)

def colourCheck(colour,defaultColour):
    # Checks if colour is valid and returns defaults if invalid
    if isinstance(colour,str):
        try:
            r,g,b = colour.split(',')
            r = int(r)
            g = int(g)
            b = int(b)
            if r > 255 or g > 255 or b > 255 or r < 0 or g < 0 or b < 0:
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

def highlightColour(colour):
    # Returns appropriate highlight colour
    r,g,b = colour
    if r > g and r > b:
        highlight = 200,50,50
    elif g > r and g > b:
        highlight = 50,200,50
    elif b > r and b > g:
        highlight = 50,50,200
    else:
        highlight = 200,200,200
    return highlight

# Colours
black = 0,0,0
white = 255,255,255
grey = 230,230,230
light_red = 255,100,100
dark_red = 128,0,0
light_blue = 173,216,230
dark_blue = 0,0,100
yellow = 200,200,0
purple = 255,0,255
green = 153,204,153
dark_green = 0,100,0
aqua = 188,212,230

# Default Colours
dark  = 0,0,0                  # black
light = 230, 230, 230          # light grey
panel_colour = 253,253,253     # off white
space_colour = 153, 204, 153   # light green
helpGreen = 100,200,100        # brighter green
highlight_colour = 240,240,240 # lighter grey
quit_colour = 200,80,80        # red

config = configparser.ConfigParser()
config.read('config.ini')

colours = config['colours']
dark  = colourCheck(colours.get('dark (P1)'),dark)
light = colourCheck(colours.get('light (P2)'),light)
space_colour = colourCheck(colours.get('board'),space_colour)
panel_colour = colourCheck(colours.get('panels'),panel_colour)

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
        if width > info.current_w or width < 1:
            width = 1280
    except ValueError:
        width = 1280
    try:
        height = int(window['height'])
        if height > info.current_h or height < 1:
            height = 800
    except ValueError:
        height = 800
size = width, height # screen size

if fullscreen:
    screen = pygame.display.set_mode(size,pygame.NOFRAME) # borderless window
else:
    screen = pygame.display.set_mode(size)
    # Resizing not ready for release
    # screen = pygame.display.set_mode(size,pygame.RESIZABLE)

# Fonts
font_small = pygame.font.Font("Quicksand-Light.ttf", 44)
font_med = pygame.font.Font("Quicksand-Light.ttf", 48)
font_large = pygame.font.Font("Quicksand-Light.ttf", 72)
font_title = pygame.font.Font("Quicksand-Light.ttf", 100)

# Screen lengths
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
spaces_surfaces = [[0 for x in range(8)] for x in range(8)]
for x in range(8):
    for y in range(8):
        spaces[x][y] = pygame.Rect((x_buffer + (side + space_buffer) * x, y_buffer + (side + space_buffer) * y),space_sides)
        spaces_surfaces[x][y] = pygame.Surface(space_sides) # space
        spaces_surfaces[x][y].fill(space_colour)

# P1's and P2's Counters
counter1 = pygame.Surface(space_sides)
counter1.fill(dark)
counter2 = pygame.Surface(space_sides)
counter2.fill(light)

highlight_alpha = 128 # out of 256 i.e. 0.5 transparency

# Help-highlighted Spaces
help_counter = pygame.Surface(space_sides)
help_counter.fill(highlightColour(space_colour))
help_counter.set_alpha(highlight_alpha)
space_help = [[0 for x in range(8)] for x in range(8)]

# Highlighted Spaces
highlight_counter = pygame.Surface(space_sides)
highlight_counter.set_alpha(highlight_alpha)
highlight_counter.fill(white)