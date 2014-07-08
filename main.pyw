import pygame
pygame.init()

import menu
import reversi

size = width, height = 1280, 800 # screen size
background = 255, 255, 255 # white

# panel_colour = 253,253,253

screen = pygame.display.set_mode(size)

# in_menu = True
# in_reversi = False
mode = {'menu':True, 'reversi':False}

#board_reversi = pygame.image.load("board_reversi.png").convert()
#board_reversi_rect = ((100,50),board_reversi.get_size())

# r0 = reversiGame()

while 1: #infinite loop
    event = pygame.event.wait() # on click
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # left click only
        if mode['menu']:
            menu.clickCheck(event.pos, mode)
            r0 = reversi.game() # i.e. new game
        elif mode['reversi']:
            reversi.clickCheck(event.pos, mode, reversi.spaces, r0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(str(event.button)) # testing mouse buttons
        #        left = 1
        #      middle = 2
        #       right = 3
        #   scroll up = 4
        # scroll down = 5
    if event.type == pygame.MOUSEMOTION:
        # if mode['menu']:
        #     asdf
        if mode['reversi']:
            reversi.mouseCheck(event.pos,r0)
        elif mode['menu']:
            menu.mouseCheck(event.pos)
    
    screen.fill(background)
    #screen.blit(board_reversi, board_reversi_rect)

    # if in_menu:
    #     menu.menuRender(screen)
    # elif in_reversi:
    #     reversi.boardRender(screen)

    if mode['menu']:
        menu.menuRender(screen)
    elif mode['reversi']:
        reversi.boardRender(screen, r0)

    pygame.display.flip()
    #pygame.time.delay(10) #delays by 1/100 of a second to slow down movement
