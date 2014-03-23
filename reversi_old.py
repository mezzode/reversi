import pygame
pygame.init()

size = width, height = 1280, 800 # screen size
background = 255, 255, 255

screen = pygame.display.set_mode(size)

space = pygame.Surface((70,70))
space.fill((0,0,0))
space_rect_0 = ((135,85),(70,70))
space_rect_1 = ((215,85),(70,70))
space_rect_2 = ((295,85),(70,70))
space_rect_3 = ((375,85),(70,70))
space_rect_4 = ((455,85),(70,70))
space_rect_5 = ((535,85),(70,70))
space_rect_6 = ((615,85),(70,70))
space_rect_7 = ((695,85),(70,70))



speed = [1,1]

board_reversi = pygame.image.load("board_reversi.png").convert()
board_reversi_rect = ((100,50),board_reversi.get_size())

while 1: #infinite loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    """board_reversi_rect = board_reversi_rect.move(speed)
    if board_reversi_rect.left < 0 or board_reversi_rect.right > width:
        speed[0] = -speed[0]
    if board_reversi_rect.top < 0 or board_reversi_rect.bottom > height:
        speed[1] = -speed[1]"""

    screen.fill(background)
    screen.blit(board_reversi, board_reversi_rect)
    screen.blit(space, space_rect_0)
    screen.blit(space, space_rect_1)
    screen.blit(space, space_rect_2)
    screen.blit(space, space_rect_3)
    screen.blit(space, space_rect_4)
    screen.blit(space, space_rect_5)
    screen.blit(space, space_rect_6)
    screen.blit(space, space_rect_7)

    pygame.display.flip()

    #pygame.time.delay(10) #delays by 1/100 of a second to slow down movement