import pygame
pygame.init()

def clickCheck (click_pos, mode):
    # Determines what should be done in response to a mouse click

    if button_return_rect.collidepoint(click_pos): # if return is clicked
        button_return_surface.fill(panel_colour)
        for m in mode:
            if m == 'reversi':
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

def rulesRender(screen):
    screen.blit(button_return_surface, button_return_rect)
    screen.blit(panel_title_surface,panel_title_rect)
    screen.blit(label_return,label_return_rect)
    screen.blit(label_title,label_title_rect)

size = width, height = 1280, 800 # screen size

font_small = pygame.font.Font("Quicksand-Light.ttf", 44)
font_med = pygame.font.Font("Quicksand-Light.ttf", 48)
font_large = pygame.font.Font("Quicksand-Light.ttf", 72)
font_title = pygame.font.Font("Quicksand-Light.ttf", 100)

panel_colour = 253,253,253

panel_title_rect = pygame.Rect((135,85),(300,100))
panel_title_surface = pygame.Surface((300,100))
panel_title_surface.fill(panel_colour)

label_title = font_large.render("Rules",1,(0,0,0))
label_title_rect = label_title.get_rect()
label_title_rect.center = (width/2,225)
label_title_rect.topleft = 135,85

button_return_rect = pygame.Rect((785,615),(360,100))
button_return_surface = pygame.Surface((360,100))
button_return_surface.fill(panel_colour)

label_return = font_med.render("Back to Game",1,(0,0,0))
label_return_rect = label_return.get_rect()
# label_return_rect.left = label_title_rect.left

# whitespace = (height - (label_title_rect.height + button_return_rect.height))/3
whitespace = height/3
# button_return_rect.top = label_title_rect.bottom + whitespace
# label_return_rect.bottom = whitespace * 2
# label_title_rect.centery = button_return_rect.top/2
# panel_title_rect.centery = button_return_rect.top/2
# label_return_rect.centery = button_return_rect.centery
# button_return_rect.centerx = label_return_rect.centerx
# label_title_rect.center = panel_title_rect.center
label_return_rect.center = button_return_rect.center