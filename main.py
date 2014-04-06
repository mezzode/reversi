import pygame
pygame.init()

import reversi

size = width, height = 1280, 800 # screen size
background = 255, 255, 255 # white

spaceColour = 153, 204, 153
spaceSides  = 70, 70  # 70 px by 70 px

screen = pygame.display.set_mode(size)

space = pygame.Surface(spaceSides)
space.fill(spaceColour)

counter1 = pygame.Surface(spaceSides)
counter1.fill((0,0,0))
counter2 = pygame.Surface(spaceSides)
counter2.fill((230,230,230))

spaces = [[0 for x in range(8)] for x in range(8)] #array init
for x in range(8):
    for y in range(8):
        spaces[x][y] = pygame.Rect((135 + 80 * x, 85 + 80 * y),spaceSides)
"""
spaces[0][0] = ((135,85),(70,70))
spaces[1][0] = ((215,85),(70,70))
spaces[2][0] = ((295,85),(70,70))
spaces[3][0] = ((375,85),(70,70))
spaces[4][0] = ((455,85),(70,70))
spaces[5][0] = ((535,85),(70,70))
spaces[6][0] = ((615,85),(70,70))
spaces[7][0] = ((695,85),(70,70))"""

space_states = [[0 for x in range(8)] for x in range(8)]
space_states[3][4] = 1
space_states[4][3] = 1
space_states[3][3] = 2
space_states[4][4] = 2
# array init
# 0 = empty, 1 = player 1 (black), 2 = player 2 (white)

#turn = 5

#board_reversi = pygame.image.load("board_reversi.png").convert()
#board_reversi_rect = ((100,50),board_reversi.get_size())

turn = 1

while 1: #infinite loop
    for event in pygame.event.get(): # this for loop should instead be a function which returns whether a space has been clicked
        if event.type == pygame.QUIT: #would be in main for loop not 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: # this should be the actual part of the function
            # mouse click coordinates in x,y
            turn = reversi.clickCheck(event.pos, spaces, space_states, turn)
    screen.fill(background)
    #screen.blit(board_reversi, board_reversi_rect)
    """
    screen.blit(space, spaces[0][0])
    screen.blit(space, spaces[1][0])
    screen.blit(space, spaces[2][0])
    screen.blit(space, spaces[3][0])
    screen.blit(space, spaces[4][0])
    screen.blit(space, spaces[5][0])
    screen.blit(space, spaces[6][0])
    screen.blit(space, spaces[7][0])"""

    for x in range(8):
        for y in range(8):
            screen.blit(space, spaces[x][y])

    for x in range(8):
        for y in range(8):
            if space_states[x][y] == 1:
                screen.blit(counter1, spaces[x][y])
            elif space_states[x][y] == 2:
                screen.blit(counter2, spaces[x][y])

    pygame.display.flip()
    #pygame.time.delay(10) #delays by 1/100 of a second to slow down movement

