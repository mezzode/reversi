import pygame
pygame.init()

import menu
import reversi

size = width, height = 1280, 800 # screen size
background = 255, 255, 255 # white

screen = pygame.display.set_mode(size)

# in_menu = True
# in_reversi = False
mode = {'menu':True, 'reversi':False}

#board_reversi = pygame.image.load("board_reversi.png").convert()
#board_reversi_rect = ((100,50),board_reversi.get_size())

while 1: #infinite loop
    event = pygame.event.wait() # on click
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        # mouse click coordinates in x,y
        # if in_menu:
        #     in_menu, in_reversi = menu.clickCheck(event.pos, in_menu, in_reversi, menu.button_play_rect)
        # elif in_reversi:
        #     reversi.turn = reversi.clickCheck(event.pos, reversi.spaces, reversi.space_states, reversi.turn)

        if mode['menu']:
            mode = menu.clickCheck(event.pos, mode, menu.button_play_rect)
        elif mode['reversi']:
            reversi.turn = reversi.clickCheck(event.pos, reversi.spaces, reversi.space_states, reversi.turn)

            # reversi.reversiCheck(event.pos)
    if event.type == pygame.MOUSEMOTION:
        # if mode['menu']:
        #     asdf
        if mode['reversi']:
            reversi.mouseCheck(event.pos)
    
    screen.fill(background)
    #screen.blit(board_reversi, board_reversi_rect)

    # if in_menu:
    #     menu.menuRender(screen)
    # elif in_reversi:
    #     reversi.boardRender(screen)

    if mode['menu']:
        menu.menuRender(screen)
    elif mode['reversi']:
        reversi.boardRender(screen,reversi.turn)

    pygame.display.flip()
    #pygame.time.delay(10) #delays by 1/100 of a second to slow down movement

