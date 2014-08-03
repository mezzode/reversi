import pygame
pygame.init()
import configparser
from common import *



def clickCheck (click_pos, mode, config):
    # Determines what should be done in response to a mouse click

    if button_return_rect.collidepoint(click_pos): # if return is clicked
        button_return_surface.fill(panel_colour)
        for m in mode:
            if m == 'menu':
                mode[m] = True
                # r0 = reversiGame()
            else:
                mode[m] = False

    if button_p1_dark_rect.collidepoint(click_pos):
        # config = configparser.ConfigParser()
        config.read('config.ini')
        # light = grey
        colours['dark (P1)'] = str(black).strip('()')
        with open('config.ini','w') as configfile: # save to config.ini
            config.write(configfile)
    
    if button_p1_blue_rect.collidepoint(click_pos):
        # config = configparser.ConfigParser()
        config.read('config.ini')
        # light = grey
        colours['dark (P1)'] = str(dark_blue).strip('()')
        with open('config.ini','w') as configfile: # save to config.ini
            config.write(configfile)

    if button_p1_red_rect.collidepoint(click_pos):
        # config = configparser.ConfigParser()
        config.read('config.ini')
        # light = grey
        colours['dark (P1)'] = str(dark_red).strip('()')
        with open('config.ini','w') as configfile: # save to config.ini
            config.write(configfile)

    if button_p2_light_rect.collidepoint(click_pos):
        # config = configparser.ConfigParser()
        config.read('config.ini')
        # light = grey
        colours['light (P2)'] = str(grey).strip('()')
        with open('config.ini','w') as configfile: # save to config.ini
            config.write(configfile)

    if button_p2_blue_rect.collidepoint(click_pos):
        # config = configparser.ConfigParser()
        config.read('config.ini')
        # light = grey
        colours['light (P2)'] = str(light_blue).strip('()')
        with open('config.ini','w') as configfile: # save to config.ini
            config.write(configfile)

    if button_p2_red_rect.collidepoint(click_pos):
        # config = configparser.ConfigParser()
        config.read('config.ini')
        # light = grey
        colours['light (P2)'] = str(light_red).strip('()')
        with open('config.ini','w') as configfile: # save to config.ini
            config.write(configfile)

    return

def mouseCheck (mouse_pos):
    # Determines what should be done in response to a mouse movement

    # template:
    # if mouse collides with button:
        # do stuff

    if button_return_rect.collidepoint(mouse_pos):
        button_return_surface.fill((240,240,240))
    else:
        button_return_surface.fill(panel_colour)
    if button_toggle_rect.collidepoint(mouse_pos):
        button_toggle_surface.fill((240,240,240))
    else:
        button_toggle_surface.fill(panel_colour)
    return

def optionsRender(screen, dark, light):

    config = configparser.ConfigParser()
    config.read('config.ini')

    colours = config['colours']
    dark  = colourCheck(colours.get('dark (P1)'),dark)
    light = colourCheck(colours.get('light (P2)'),light)

    button_p1_current_surface.fill(dark)
    button_p2_current_surface.fill(light)

    screen.blit(button_return_surface, button_return_rect)
    # screen.blit(panel_title_surface,panel_title_rect)
    screen.blit(label_return,label_return_rect)
    screen.blit(label_title,label_title_rect)
    screen.blit(label_display,label_display_rect)
    # screen.blit(label_rules_1,label_rules_1_rect)
    # screen.blit(label_rules_2,label_rules_2_rect)
    # screen.blit(label_rules_3,label_rules_3_rect)
    # screen.blit(label_rules_4,label_rules_4_rect)
    # screen.blit(label_rules_5,label_rules_5_rect)

    screen.blit(button_toggle_surface,button_toggle_rect)
    screen.blit(label_toggle,label_toggle_rect)

    screen.blit(label_p1_title,label_p1_title_rect)
    screen.blit(button_p1_current_surface,button_p1_current_rect)
    screen.blit(button_p1_dark_surface,button_p1_dark_rect)
    screen.blit(button_p1_red_surface,button_p1_red_rect)
    screen.blit(button_p1_blue_surface,button_p1_blue_rect)

    screen.blit(label_p2_title,label_p2_title_rect)
    screen.blit(button_p2_current_surface,button_p2_current_rect)
    screen.blit(button_p2_light_surface,button_p2_light_rect)
    screen.blit(button_p2_blue_surface,button_p2_blue_rect)
    screen.blit(button_p2_red_surface,button_p2_red_rect)

    screen.blit(label_p1_selection,label_p1_selection_rect)
    screen.blit(label_p2_selection,label_p2_selection_rect)

panel_title_rect = pygame.Rect((135,85),(300,100))
panel_title_surface = pygame.Surface((300,100))
panel_title_surface.fill(panel_colour)

label_title = font_large.render("Options",1,(0,0,0))
label_title_rect = label_title.get_rect()
# label_title_rect.center = (width/2,225)
# label_title_rect.topleft = 135,85
label_title_rect.topleft = x_buffer,y_buffer

label_p1_title = font_med.render("P1's Colour",1,black)
label_p1_title_rect = label_p1_title.get_rect()

label_p2_title = font_med.render("P2's Colour",1,black)
label_p2_title_rect = label_p2_title.get_rect()

button_return_rect = pygame.Rect((785,615),(360,panel_height))
button_return_rect.right = width - x_buffer
button_return_rect.bottom = height - y_buffer
button_return_surface = pygame.Surface((360,panel_height))
button_return_surface.fill(panel_colour)

label_return = font_med.render("Back to Menu",1,(0,0,0))
label_return_rect = label_return.get_rect()
# label_return_rect.left = label_title_rect.left

label_rules_1 = font_small.render("Take enemy pieces by placing one of your ",1,(0,0,0))
label_rules_2 = font_small.render("own to trap their pieces between the one you",1,(0,0,0))
label_rules_3 = font_small.render("just placed and another one of your pieces.",1,(0,0,0))
label_rules_4 = font_small.render("Whoever has the most pieces when neither ",1,(0,0,0))
label_rules_5 = font_small.render("player can make a move wins!",1,(0,0,0))
label_rules_1_rect = label_rules_1.get_rect()
label_rules_2_rect = label_rules_2.get_rect()
label_rules_3_rect = label_rules_3.get_rect()
label_rules_4_rect = label_rules_4.get_rect()
label_rules_5_rect = label_rules_5.get_rect()
label_rules_1_rect.topleft = label_title_rect.bottomleft
label_rules_1_rect.top = label_rules_1_rect.top + 20
label_rules_2_rect.topleft = label_rules_1_rect.bottomleft
label_rules_3_rect.topleft = label_rules_2_rect.bottomleft
label_rules_4_rect.topleft = label_rules_3_rect.bottomleft
label_rules_4_rect.top = label_rules_4_rect.top + 15
label_rules_5_rect.topleft = label_rules_4_rect.bottomleft

label_return_rect.center = button_return_rect.center

# P1 Colours

label_p1_title_rect.left = label_title_rect.left
label_p1_title_rect.top = label_title_rect.bottom + controls_buffer

button_p1_current_rect = pygame.Rect((label_p1_title_rect.left, label_p1_title_rect.bottom + controls_buffer),space_sides)
button_p1_current_surface = pygame.Surface(space_sides)
button_p1_current_surface.fill(dark)

button_p1_dark_rect = pygame.Rect((label_p1_title_rect.left, label_p1_title_rect.bottom + controls_buffer),space_sides)
button_p1_dark_surface = pygame.Surface(space_sides)
button_p1_dark_surface.fill(black)
button_p1_dark_rect.left = button_p1_current_rect.right + side # controls_buffer * 3

button_p1_blue_rect = pygame.Rect((label_p1_title_rect.left, label_p1_title_rect.bottom + controls_buffer),space_sides)
button_p1_blue_surface = pygame.Surface(space_sides)
button_p1_blue_surface.fill(dark_blue)
button_p1_blue_rect.left = button_p1_dark_rect.right + controls_buffer

button_p1_red_rect = pygame.Rect((label_p1_title_rect.left, label_p1_title_rect.bottom + controls_buffer),space_sides)
button_p1_red_surface = pygame.Surface(space_sides)
button_p1_red_surface.fill(dark_red)
button_p1_red_rect.left = button_p1_blue_rect.right + controls_buffer

# P2 Colours

label_p2_title_rect.left = label_title_rect.left
label_p2_title_rect.top = button_p1_current_rect.bottom + controls_buffer

button_p2_current_rect = pygame.Rect((label_p1_title_rect.left, label_p2_title_rect.bottom + controls_buffer),space_sides)
button_p2_current_surface = pygame.Surface(space_sides)
button_p2_current_surface.fill(light)

button_p2_light_rect = pygame.Rect((label_p2_title_rect.left, label_p2_title_rect.bottom + controls_buffer),space_sides)
button_p2_light_surface = pygame.Surface(space_sides)
button_p2_light_surface.fill(grey)
button_p2_light_rect.left = button_p2_current_rect.right + side

button_p2_blue_rect = pygame.Rect((label_p2_title_rect.left, label_p2_title_rect.bottom + controls_buffer),space_sides)
button_p2_blue_surface = pygame.Surface(space_sides)
button_p2_blue_surface.fill(light_blue)
button_p2_blue_rect.left = button_p2_light_rect.right + controls_buffer

button_p2_red_rect = pygame.Rect((label_p2_title_rect.left, label_p2_title_rect.bottom + controls_buffer),space_sides)
button_p2_red_surface = pygame.Surface(space_sides)
button_p2_red_surface.fill(light_red)
button_p2_red_rect.left = button_p2_blue_rect.right + controls_buffer

# Selections Labels

label_p1_selection = font_small.render("P1",1,white)
label_p1_selection_rect = label_p1_selection.get_rect()
label_p1_selection_rect.center = button_p1_current_rect.center

label_p2_selection = font_small.render("P2",1,black)
label_p2_selection_rect = label_p2_selection.get_rect()
label_p2_selection_rect.center = button_p2_current_rect.center

# Display

label_display = font_med.render("Display",1,black)
label_display_rect = label_display.get_rect()
label_display_rect.right = width - x_buffer
label_display_rect.top = label_title_rect.bottom + controls_buffer

button_toggle_rect = pygame.Rect((785,615),(360,panel_height))
button_toggle_rect.right = width - x_buffer
button_toggle_rect.top = label_display_rect.bottom + controls_buffer
button_toggle_surface = pygame.Surface((360,panel_height))
button_toggle_surface.fill(panel_colour)

label_toggle = font_small.render("Fullscreen",1,black)
label_toggle_rect = label_toggle.get_rect()
label_toggle_rect.center = button_toggle_rect.center