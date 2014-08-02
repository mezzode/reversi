import pygame
pygame.init()
from common import *

def clickCheck (click_pos, mode):
    # Determines what should be done in response to a mouse click

    if button_return_rect.collidepoint(click_pos): # if return is clicked
        button_return_surface.fill(panel_colour)
        for m in mode:
            if m == 'menu':
                mode[m] = True
                # r0 = reversiGame()
            else:
                mode[m] = False
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
    return

def optionsRender(screen):
    screen.blit(button_return_surface, button_return_rect)
    # screen.blit(panel_title_surface,panel_title_rect)
    screen.blit(label_return,label_return_rect)
    screen.blit(label_title,label_title_rect)
    screen.blit(label_rules_1,label_rules_1_rect)
    screen.blit(label_rules_2,label_rules_2_rect)
    screen.blit(label_rules_3,label_rules_3_rect)
    screen.blit(label_rules_4,label_rules_4_rect)
    screen.blit(label_rules_5,label_rules_5_rect)

panel_title_rect = pygame.Rect((135,85),(300,100))
panel_title_surface = pygame.Surface((300,100))
panel_title_surface.fill(panel_colour)

label_title = font_large.render("Options",1,(0,0,0))
label_title_rect = label_title.get_rect()
# label_title_rect.center = (width/2,225)
# label_title_rect.topleft = 135,85
label_title_rect.topleft = x_buffer,y_buffer

button_return_rect = pygame.Rect((785,615),(360,100))
button_return_rect.right = width - x_buffer
button_return_rect.bottom = height - y_buffer
button_return_surface = pygame.Surface((360,100))
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

button_p1_black_rect = pygame.Rect((label_title_rect.left, label_title_rect.bottom + controls_buffer),space_sides)
button_p1_black_surface = pygame.Surface(space_sides)
button_p1_black_surface.fill(black)