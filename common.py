import pygame
pygame.init()

# if os.path.isfile('')
# if config file doesnt exist:
import configparser
config = configparser.ConfigParser()
# config['DEFAULT'] = {} # default values for each section here
config['colours'] = {}
colours = config['colours']
# colours['dark'] = '0,0,0'
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

def strToColour(colourStr):
    r,g,b = colourStr.split(',')
    r = int(r)
    g = int(g)
    b = int(b)
    colour = r,g,b
    return colour

# Colours
black = 0,0,0
white = 255,255,255
red = 255,100,100
purple = 255,0,255
blue = 0,0,100
yellow = 200,200,0
# dark  = 0,0,0                  # black
# light = 230, 230, 230          # light grey
# panel_colour = 253,253,253     # off white
# space_colour = 153, 204, 153   # light green
# helpGreen = 100,200,100        # brighter green
# highlight_colour = 240,240,240 # lighter grey

dark_defaults = {'black':black, 'red':red, 'purple':purple}
light_defaults = {'white':white, 'blue':blue, 'yellow':yellow}

config = configparser.ConfigParser()
config.read('config.ini')

colours = config['colours']
dark  = colours.get('dark',black)
light = strToColour(colours['light'])
space_colour = strToColour(colours['space_colour'])
helpGreen = strToColour(colours['help_colour'])
panel_colour = strToColour(colours['panel_colour'])
highlight_colour = strToColour(colours['highlight_colour'])

window = config['window']
width = int(window['width'])
height = int(window['height'])
size = width, height # screen size

# Fonts
font_small = pygame.font.Font("Quicksand-Light.ttf", 44)
font_med = pygame.font.Font("Quicksand-Light.ttf", 48)