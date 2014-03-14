import pygame
pygame.init()

size = width, height = 1280, 800 # screen size
"""black = 0, 0, 0

screen = pygame.display.set_mode(size)

speed = [1,1]

board_reversi = pygame.image.load("board_reversi.png").convert()
board_reversi_rect = board_reversi.get_rect()

while 1: #infinite loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    board_reversi_rect = board_reversi_rect.move(speed)
    if board_reversi_rect.left < 0 or board_reversi_rect.right > width:
        speed[0] = -speed[0]
    if board_reversi_rect.top < 0 or board_reversi_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(board_reversi, board_reversi_rect)
    pygame.display.flip()

    pygame.time.delay(10) #delays by 1/100 of a second to slow down movement"""

#on mouse click of a space (x,y) - requires space coordinates and current player

#check if valid move ... make separate subroutine?
valid_move = True
board_state = #2D array i.e. 0-7,0-7
#direction 1: up
while valid_move = True and y < 8: #must stop when reaches edge of board
    y = y + 1
    if board_state[x,y] != #enemy_num? ... also, check actual array syntax
        valid_move = False
#etc.

