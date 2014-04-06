import pygame
pygame.init()

import menu
import reversi

size = width, height = 1280, 800 # screen size
background = 255, 255, 255 # white

screen = pygame.display.set_mode(size)

in_menu = True
in_reversi = False

#board_reversi = pygame.image.load("board_reversi.png").convert()
#board_reversi_rect = ((100,50),board_reversi.get_size())

while 1: #infinite loop
    for event in pygame.event.get(): # on click
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # mouse click coordinates in x,y
            if in_menu:
                in_menu, in_reversi = menu.clickCheck(event.pos, in_menu, in_reversi, menu.button_play_rect)
            if in_reversi:
                # reversi.reversiCheck(event.pos)
                reversi.turn = reversi.clickCheck(event.pos, reversi.spaces, reversi.space_states, reversi.turn)
    
    screen.fill(background)
    #screen.blit(board_reversi, board_reversi_rect)

    if in_menu:
        menu.menuRender(screen)
    elif in_reversi:
        reversi.boardRender(screen)

    pygame.display.flip()
    #pygame.time.delay(10) #delays by 1/100 of a second to slow down movement

