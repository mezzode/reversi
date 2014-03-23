import pygame
pygame.init()

size = width, height = 1280, 800 # screen size
background = 255, 255, 255

screen = pygame.display.set_mode(size)

space = pygame.Surface((70,70))
space.fill((0,0,0))

spaces = [[0 for x in range(8)] for x in range(8)] #array init
for x in range(8):
    for y in range(8):
        spaces[x][y] = pygame.Rect((135 + 80 * x, 85 + 80 * y),(70,70))
"""
spaces[0][0] = ((135,85),(70,70))
spaces[1][0] = ((215,85),(70,70))
spaces[2][0] = ((295,85),(70,70))
spaces[3][0] = ((375,85),(70,70))
spaces[4][0] = ((455,85),(70,70))
spaces[5][0] = ((535,85),(70,70))
spaces[6][0] = ((615,85),(70,70))
spaces[7][0] = ((695,85),(70,70))"""

#board_reversi = pygame.image.load("board_reversi.png").convert()
#board_reversi_rect = ((100,50),board_reversi.get_size())

while 1: #infinite loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # mouse click coordinates in x,y
            click_pos = event.pos
            for x in range(8):
                for y in range(8):
                    if spaces[x][y].collidepoint(click_pos):
                        #pass x,y into validMoveCheck
                        print("ninjas", x, y) #just a thing to close the if block

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

    pygame.display.flip()
    #pygame.time.delay(10) #delays by 1/100 of a second to slow down movement