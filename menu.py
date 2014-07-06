import pygame
pygame.init()

# note for future: rects do not need to be passed in

def mouseCheck (event, mouse_pos, mode):
    if button_play_rect.collidepoint(mouse_pos):
        # in_menu = False
        # in_reversi = True
        # print (test)
        for m in mode:
            if m == 'reversi':
                mode[m] = True
                # r0 = reversiGame()
            else:
                mode[m] = False
    return;

def menuRender(screen):
    
    
    """
    button_play_rect = button_play_rect.move(speed)
    if button_play_rect.left < 0 or button_play_rect.right > width:
        speed[0] = -speed[0]
    if button_play_rect.top < 0 or button_play_rect.bottom > height:
        speed[1] = -speed[1]"""

    screen.blit(button_play, button_play_rect)

    #pygame.display.flip()

    #pygame.time.delay(10) #delays by 1/100 of a second to slow down movement

button_play = pygame.image.load("button_play.png")#.convert()
button_play_rect = button_play.get_rect(center = (640,400))

test = "moo"