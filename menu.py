import pygame
pygame.init()
from common import *

# note for future: rects do not need to be passed in

def clickCheck (click_pos, mode):
    # Determines what should be done in response to a mouse click
    running = True
    if button_play_rect.collidepoint(click_pos): # if play is clicked
        button_play_surface.fill(panel_colour)
        for m in mode:
            if m == 'reversi':
                mode[m] = True
                # r0 = reversiGame()
            else:
                mode[m] = False
    if button_exit_rect.collidepoint(click_pos): # if exit is clicked
        running = False
        # pygame.quit()
        # sys.exit()
    if button_options_rect.collidepoint(click_pos): # if options is clicked
        button_options_surface.fill(panel_colour)
        for m in mode:
            if m == 'options':
                mode[m] = True
            else:
                mode[m] = False
    return running

def mouseCheck (mouse_pos):
    # Determines what should be done in response to a mouse movement

    # template:
    # if mouse collides with button:
        # do stuff

    if button_play_rect.collidepoint(mouse_pos):
        button_play_surface.fill((240,240,240))
    else:
        button_play_surface.fill(panel_colour)

    if button_exit_rect.collidepoint(mouse_pos):
        # button_help_surface.fill((230,230,230))
        button_exit_surface.fill((240,240,240))
    else:
        button_exit_surface.fill(panel_colour)

    if button_options_rect.collidepoint(mouse_pos):
        # button_help_surface.fill((230,230,230))
        button_options_surface.fill((240,240,240))
    else:
        button_options_surface.fill(panel_colour)

    return

def menuRender(screen):
    screen.blit(button_play_surface, button_play_rect)
    screen.blit(button_exit_surface, button_exit_rect)
    screen.blit(button_options_surface, button_options_rect)
    # screen.blit(panel_title_surface,panel_title_rect)
    screen.blit(label_play,label_play_rect)
    screen.blit(label_exit,label_exit_rect)
    screen.blit(label_options,label_options_rect)
    screen.blit(label_title,label_title_rect)

# size = width, height = 1280, 800 # screen size

# font_small = pygame.font.Font("Quicksand-Light.ttf", 44)
# font_med = pygame.font.Font("Quicksand-Light.ttf", 48)
# font_large = pygame.font.Font("Quicksand-Light.ttf", 72)
# font_title = pygame.font.Font("Quicksand-Light.ttf", 100)

# panel_colour = 253,253,253

panel_title_rect = pygame.Rect(((width-700)/2,100),(700,150))
panel_title_surface = pygame.Surface((700,150))
panel_title_surface.fill(panel_colour)

label_title = font_title.render("Reversi 2014",1,(0,0,0))
label_title_rect = label_title.get_rect()
label_title_rect.midbottom = (width/2,height/3)

# button_play = pygame.image.load("button_play.png")#.convert()
# button_play_rect = button_play.get_rect(center = (640,400))
button_play_rect = pygame.Rect((490,450),(300,100))
button_play_surface = pygame.Surface((300,100))
button_play_surface.fill(panel_colour)

label_play = font_large.render("Play",1,(0,0,0))
label_play_rect = label_play.get_rect()
label_play_rect.left = label_title_rect.left

button_exit_rect = pygame.Rect((490,450),(300,100))
button_exit_surface = pygame.Surface((300,100))
button_exit_surface.fill(panel_colour)

label_exit = font_large.render("Exit",1,(0,0,0))
label_exit_rect = label_exit.get_rect()
label_exit_rect.right = label_title_rect.right

button_options_rect = pygame.Rect((490,450),(300,100))
button_options_surface = pygame.Surface((300,100))
button_options_surface.fill(panel_colour)

label_options = font_large.render("Options",1,(0,0,0))
label_options_rect = label_options.get_rect()
label_options_rect.right = label_title_rect.right


# whitespace = (height - (label_title_rect.height + button_play_rect.height))/3
# whitespace = height/3
# button_play_rect.top = label_title_rect.bottom + whitespace
button_play_rect.bottom = height * (2/3) # whitespace * 2
button_exit_rect.bottom = height * (2/3) # whitespace * 2
button_options_rect.bottom = height * (2/3)
panel_title_rect.centery = button_play_rect.top/2
# move labels to same height as buttons
label_play_rect.centery = button_play_rect.centery
label_exit_rect.centery = button_exit_rect.centery
# move buttons sideways so that the labels are centred
button_play_rect.centerx = label_play_rect.centerx
button_exit_rect.centerx = label_exit_rect.centerx

button_play_rect.centerx = label_title_rect.left
button_exit_rect.centerx = label_title_rect.right
label_play_rect.center = button_play_rect.center
label_exit_rect.center = button_exit_rect.center

button_options_rect.centerx = panel_title_rect.centerx
label_options_rect.center = button_options_rect.center