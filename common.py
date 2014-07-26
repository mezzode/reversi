import pygame
pygame.init()

# if os.path.isfile('')
# if config file doesnt exist:
import configparser
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
# dark  = 0,0,0                  # black
# light = 230, 230, 230          # light grey
# panel_colour = 253,253,253     # off white
# space_colour = 153, 204, 153   # light green
# helpGreen = 100,200,100        # brighter green
# highlight_colour = 240,240,240 # lighter grey

config = configparser.ConfigParser()
config.read('config.ini')
colours = config['colours']
dark  = strToColour(colours['dark'])
light = strToColour(colours['light'])
space_colour = strToColour(colours['space_colour'])
helpGreen = strToColour(colours['help_colour'])
panel_colour = strToColour(colours['panel_colour'])
highlight_colour = strToColour(colours['highlight_colour'])

# Fonts
font_small = pygame.font.Font("Quicksand-Light.ttf", 44)
font_med = pygame.font.Font("Quicksand-Light.ttf", 48)