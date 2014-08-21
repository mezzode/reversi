import pygame
pygame.init()
import configparser
from common import *

def clickCheck (click_pos, mode, config):
    # Determines what should be done in response to a mouse click

    if button_return_rect.collidepoint(click_pos):
        # if return is clicked
        button_return_surface.fill(panel_colour)
        for m in mode:
            if m == 'menu':
                mode[m] = True
            else:
                mode[m] = False

    if button_toggle_rect.collidepoint(click_pos):
        # if screen toggle is clicked
        config.read('config.ini')
        if window.getboolean('fullscreen'):
            window['fullscreen'] = 'False'
        else:
            window['fullscreen'] = 'True'
        with open('config.ini','w') as configfile: # save to config.ini
            config.write(configfile)

    if button_p1_dark_rect.collidepoint(click_pos):
        config.read('config.ini')
        colours['dark (P1)'] = str(black).strip('()')
        with open('config.ini','w') as configfile: # save to config.ini
            config.write(configfile)
    
    if button_p1_blue_rect.collidepoint(click_pos):
        config.read('config.ini')
        colours['dark (P1)'] = str(dark_blue).strip('()')
        with open('config.ini','w') as configfile: # save to config.ini
            config.write(configfile)

    if button_p1_red_rect.collidepoint(click_pos):
        config.read('config.ini')
        colours['dark (P1)'] = str(dark_red).strip('()')
        with open('config.ini','w') as configfile: # save to config.ini
            config.write(configfile)

    if button_p2_light_rect.collidepoint(click_pos):
        config.read('config.ini')
        colours['light (P2)'] = str(grey).strip('()')
        with open('config.ini','w') as configfile: # save to config.ini
            config.write(configfile)

    if button_p2_blue_rect.collidepoint(click_pos):
        config.read('config.ini')
        colours['light (P2)'] = str(light_blue).strip('()')
        with open('config.ini','w') as configfile: # save to config.ini
            config.write(configfile)

    if button_p2_red_rect.collidepoint(click_pos):
        config.read('config.ini')
        colours['light (P2)'] = str(light_red).strip('()')
        with open('config.ini','w') as configfile: # save to config.ini
            config.write(configfile)

    if button_board_green_rect.collidepoint(click_pos):
        config.read('config.ini')
        colours['board'] = str(green).strip('()')
        with open('config.ini','w') as configfile: # save to config.ini
            config.write(configfile)

    if button_board_aqua_rect.collidepoint(click_pos):
        config.read('config.ini')
        colours['board'] = str(aqua).strip('()')
        with open('config.ini','w') as configfile: # save to config.ini
            config.write(configfile)

    if button_board_dark_rect.collidepoint(click_pos):
        config.read('config.ini')
        colours['board'] = str(dark_green).strip('()')
        with open('config.ini','w') as configfile: # save to config.ini
            config.write(configfile)

    return

def mouseCheck (mouse_pos, highlight_alpha):
    # Determines what should be done in response to a mouse movement

    if button_return_rect.collidepoint(mouse_pos):
        button_return_surface.fill((240,240,240))
    else:
        button_return_surface.fill(panel_colour)
    if button_toggle_rect.collidepoint(mouse_pos):
        button_toggle_surface.fill((240,240,240))
    else:
        button_toggle_surface.fill(panel_colour)

    if button_p1_dark_rect.collidepoint(mouse_pos):
        button_p1_dark_surface.set_alpha(highlight_alpha)
    else:
        button_p1_dark_surface.set_alpha()
    if button_p1_red_rect.collidepoint(mouse_pos):
        button_p1_red_surface.set_alpha(highlight_alpha)
    else:
        button_p1_red_surface.set_alpha()
    if button_p1_blue_rect.collidepoint(mouse_pos):
        button_p1_blue_surface.set_alpha(highlight_alpha)
    else:
        button_p1_blue_surface.set_alpha()

    if button_p2_light_rect.collidepoint(mouse_pos):
        button_p2_light_surface.set_alpha(highlight_alpha)
    else:
        button_p2_light_surface.set_alpha()
    if button_p2_red_rect.collidepoint(mouse_pos):
        button_p2_red_surface.set_alpha(highlight_alpha)
    else:
        button_p2_red_surface.set_alpha()
    if button_p2_blue_rect.collidepoint(mouse_pos):
        button_p2_blue_surface.set_alpha(highlight_alpha)
    else:
        button_p2_blue_surface.set_alpha()

    if button_board_green_rect.collidepoint(mouse_pos):
        button_board_green_surface.set_alpha(highlight_alpha)
    else:
        button_board_green_surface.set_alpha()
    if button_board_aqua_rect.collidepoint(mouse_pos):
        button_board_aqua_surface.set_alpha(highlight_alpha)
    else:
        button_board_aqua_surface.set_alpha()
    if button_board_dark_rect.collidepoint(mouse_pos):
        button_board_dark_surface.set_alpha(highlight_alpha)
    else:
        button_board_dark_surface.set_alpha()

    return

def optionsRender(screen, dark, light, space_colour, fullscreen):

    config = configparser.ConfigParser()
    config.read('config.ini')

    colours = config['colours']
    dark  = colourCheck(colours.get('dark (P1)'),dark)
    light = colourCheck(colours.get('light (P2)'),light)
    space_colour = colourCheck(colours.get('board'),space_colour)

    button_p1_current_surface.fill(dark)
    button_p2_current_surface.fill(light)
    button_board_current_surface.fill(space_colour)
    window = config['window']
    try:
        fullscreen = window.getboolean('fullscreen')
    except ValueError:
        fullscreen = False
    if fullscreen:
        label_toggle = font_small.render("Fullscreen",1,black)
        if not fullscreen:
            screen.blit(label_restart_1,label_restart_1_rect)
            screen.blit(label_restart_2,label_restart_2_rect)
    else:
        label_toggle = font_small.render("Windowed",1,black)
        if fullscreen:
            screen.blit(label_restart_1,label_restart_1_rect)
            screen.blit(label_restart_2,label_restart_2_rect)
    label_toggle_rect = label_toggle.get_rect()
    label_toggle_rect.center = button_toggle_rect.center

    screen.blit(button_return_surface, button_return_rect)
    # screen.blit(panel_title_surface,panel_title_rect)
    screen.blit(label_return,label_return_rect)
    screen.blit(label_title,label_title_rect)
    screen.blit(label_display,label_display_rect)

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

    screen.blit(label_board,label_board_rect)
    screen.blit(button_board_current_surface,button_board_current_rect)
    screen.blit(button_board_green_surface,button_board_green_rect)
    screen.blit(button_board_aqua_surface,button_board_aqua_rect)
    screen.blit(button_board_dark_surface,button_board_dark_rect)

    screen.blit(label_p1_selection,label_p1_selection_rect)
    screen.blit(label_p2_selection,label_p2_selection_rect)

#############################
# Permanent Screen Elements #
#############################

# Sections
panel_title_rect = pygame.Rect((135,85),(300,100))
panel_title_surface = pygame.Surface((300,100))
panel_title_surface.fill(panel_colour)
label_title = font_large.render("Options",1,black)
label_title_rect = label_title.get_rect()
label_title_rect.topleft = x_buffer,y_buffer

label_p1_title = font_med.render("P1's Colour",1,black)
label_p1_title_rect = label_p1_title.get_rect()

label_p2_title = font_med.render("P2's Colour",1,black)
label_p2_title_rect = label_p2_title.get_rect()

label_board = font_med.render("Board Colour",1,black)
label_board_rect = label_board.get_rect()

# Display

label_display = font_med.render("Display",1,black)
label_display_rect = label_display.get_rect()
label_display_rect.right = width - x_buffer
label_display_rect.top = label_title_rect.bottom + controls_buffer

button_toggle_rect = pygame.Rect((785,615),(360,panel_height))
button_toggle_rect.right = label_display_rect.right
button_toggle_rect.top = label_display_rect.bottom + controls_buffer
button_toggle_surface = pygame.Surface((360,panel_height))
button_toggle_surface.fill(panel_colour)

label_toggle = font_small.render("Fullscreen",1,black)
label_toggle_rect = label_toggle.get_rect()
label_toggle_rect.center = button_toggle_rect.center

label_restart_1 = font_small.render("You must restart for",1,black)
label_restart_1_rect = label_restart_1.get_rect()
label_restart_1_rect.top = button_toggle_rect.bottom + controls_buffer
label_restart_1_rect.right = label_display_rect.right

label_restart_2 = font_small.render("changes to take effect",1,black)
label_restart_2_rect = label_restart_2.get_rect()
label_restart_2_rect.top = label_restart_1_rect.bottom + 10
label_restart_2_rect.right = label_display_rect.right

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

# Board Colours

label_board_rect.left = label_title_rect.left
label_board_rect.top = button_p2_current_rect.bottom + controls_buffer

button_board_current_rect = pygame.Rect((label_board_rect.left, label_board_rect.bottom + controls_buffer),space_sides)
button_board_current_surface = pygame.Surface(space_sides)
button_board_current_surface.fill(space_colour)

button_board_green_rect = pygame.Rect((label_board_rect.left, label_board_rect.bottom + controls_buffer),space_sides)
button_board_green_surface = pygame.Surface(space_sides)
button_board_green_surface.fill(green)
button_board_green_rect.left = button_board_current_rect.right + side

button_board_aqua_rect = pygame.Rect((label_board_rect.left, label_board_rect.bottom + controls_buffer),space_sides)
button_board_aqua_surface = pygame.Surface(space_sides)
button_board_aqua_surface.fill(aqua)
button_board_aqua_rect.left = button_board_green_rect.right + controls_buffer

button_board_dark_rect = pygame.Rect((label_board_rect.left, label_board_rect.bottom + controls_buffer),space_sides)
button_board_dark_surface = pygame.Surface(space_sides)
button_board_dark_surface.fill(dark_green)
button_board_dark_rect.left = button_board_aqua_rect.right + controls_buffer

button_return_rect = pygame.Rect((785,615),(360,panel_height))
button_return_rect.right = width - x_buffer
button_return_rect.bottom = button_board_current_rect.bottom # height - y_buffer
button_return_surface = pygame.Surface((360,panel_height))
button_return_surface.fill(panel_colour)

label_return = font_med.render("Back to Menu",1,black)
label_return_rect = label_return.get_rect()
# label_return_rect.left = label_title_rect.left

label_return_rect.center = button_return_rect.center