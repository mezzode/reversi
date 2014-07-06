import pygame
pygame.init()

# note for future: rects do not need to be passed in

def clickCheck (click_pos, mode):
    if button_play_rect.collidepoint(click_pos): # if play is clicked
        # in_menu = False
        # in_reversi = True
        # print (test)
        for m in mode:
            if m == 'reversi':
                mode[m] = True
                # r0 = reversiGame()
            else:
                mode[m] = False
    # if button_settings_rect.collidepoint(click_pos): # if settings is clicked
    #     # in_menu = False
    #     # in_reversi = True
    #     for m in mode:
    #         if m == 'settings':
    #             mode[m] = True
    #         else:
    #             mode[m] = False
    return;

def menuRender(screen):
    
    """
    button_play_rect = button_play_rect.move(speed)
    if button_play_rect.left < 0 or button_play_rect.right > width:
        speed[0] = -speed[0]
    if button_play_rect.top < 0 or button_play_rect.bottom > height:
        speed[1] = -speed[1]"""

    screen.blit(button_play_surface, button_play_rect)
    screen.blit(label_play,label_play_rect)

    #pygame.display.flip()

    #pygame.time.delay(10) #delays by 1/100 of a second to slow down movement

font_small = pygame.font.Font("Quicksand-Light.ttf", 44)
font_med = pygame.font.Font("Quicksand-Light.ttf", 48)

panel_colour = 253,253,253

# button_play = pygame.image.load("button_play.png")#.convert()
# button_play_rect = button_play.get_rect(center = (640,400))
button_play_rect = pygame.Rect((490,350),(300,100))
button_play_surface = pygame.Surface((300,100))
button_play_surface.fill(panel_colour)

label_play = font_med.render("Play",1,(0,0,0))
label_play_rect = label_play.get_rect()
label_play_rect.center = button_play_rect.center


test = "moo"
