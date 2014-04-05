import pygame
pygame.init()

size = width, height = 1280, 800 # screen size
background = 255, 255, 255

spaceColour = 153, 204, 153 # black
spaceSides  = 70, 70  # 70 px by 70 px

screen = pygame.display.set_mode(size)

space = pygame.Surface(spaceSides)
space.fill(spaceColour)

counter1 = pygame.Surface(spaceSides)
counter1.fill((0,0,0))
counter2 = pygame.Surface(spaceSides)
counter2.fill((200,200,200))

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

def currentPlayer(turn):
    if turn % 2 == 1: # if turn is odd
        player = 1
        enemy  = 2
    else:
        player = 2
        enemy  = 1
    return (player, enemy)

def clickCheck (click_pos, space_states, turn):
    for x in range(8): #beginning of important part of function code
        for y in range(8):
            if spaces[x][y].collidepoint(click_pos):
                # pass x,y into moveCheck
                turn = moveCheck(x,y,space_states, turn)
                #print("ninjas", x, y) #just a thing to close the if block
    # if collides with buttons or other clickable things:
        # do stuff
    return turn;

def spaceCheck (x,y,space_states, turn, to_flip, flip_buffer):
    player, enemy = currentPlayer(turn)
    if space_states[x][y] == enemy:
        flip_buffer.append((x,y))
        done = False
    elif space_states[x][y] == player and len(flip_buffer) > 0:
        to_flip.extend(flip_buffer)
        flip_buffer = []
        done = True
    else:
        flip_buffer = []
        done = True
    return done;

def moveMaker (space_states, to_flip, turn):
    player, enemy = currentPlayer(turn)
    for xy in to_flip:
        x, y = xy
        space_states[x][y] = player
    turn += 1
    return turn

def moveCheck (x,y, space_states, turn):
    xy = x, y
    to_flip = []
    flip_buffer = []

    if space_states[x][y] == 0: #empty
        valid_move = True
    else:
        valid_move = False
    
    if valid_move:
        #check north
        done = False
        x, y = xy
        while y > 0 and done == False:
            y += -1
            done = spaceCheck (x,y,space_states,turn, to_flip, flip_buffer)
        flip_buffer = []
        print(to_flip, flip_buffer)
        
        #check south
        done = False
        x, y = xy
        while y < 7 and done == False:
            y += 1
            done = spaceCheck (x,y,space_states,turn, to_flip, flip_buffer)
        flip_buffer = []
        print(to_flip, flip_buffer)
        
        #check east
        done = False
        x, y = xy
        while x < 7 and done == False:
            x += 1
            done = spaceCheck (x,y,space_states,turn, to_flip, flip_buffer)
        flip_buffer = []
        print(to_flip, flip_buffer)
        
        #check west
        done = False
        x, y = xy
        while x > 0 and done == False:
            x += -1
            done = spaceCheck (x,y,space_states,turn, to_flip, flip_buffer)
        flip_buffer = []
        print(to_flip, flip_buffer)
        
        #check NE
        done = False
        x, y = xy
        while y > 0 and x < 7 and done == False:
            x += 1
            y += -1
            done = spaceCheck (x,y,space_states,turn, to_flip, flip_buffer)
        flip_buffer = []
        print(to_flip, flip_buffer)
        
        #check SE
        done = False
        x, y = xy
        while y < 7 and x < 7 and done == False:
            x += 1
            y += 1
            done = spaceCheck (x,y,space_states,turn, to_flip, flip_buffer)
        flip_buffer = []
        print(to_flip, flip_buffer)
        
        #check SW
        done = False
        x, y = xy
        while y < 7 and x > 0 and done == False:
            x += -1
            y += 1
            done = spaceCheck (x,y,space_states,turn, to_flip, flip_buffer)
        flip_buffer = []
        print(to_flip, flip_buffer)
        
        #check NW
        done = False
        x, y = xy
        while y > 0 and x > 0 and done == False:
            x += -1
            y += -1
            done = spaceCheck (x,y,space_states,turn, to_flip, flip_buffer)
        flip_buffer = []
        print(to_flip, flip_buffer)
        
        if len(to_flip) == 0:
            valid_move = False

        if valid_move:
            to_flip.append(xy)

            print(to_flip, flip_buffer)
            turn = moveMaker(space_states, to_flip, turn)
    return turn;

turn = 5

while 1: #infinite loop
    for event in pygame.event.get(): # this for loop should instead be a function which returns whether a space has been clicked
        if event.type == pygame.QUIT: #would be in main for loop not 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: # this should be the actual part of the function
            # mouse click coordinates in x,y
            turn = clickCheck(event.pos, space_states, turn)
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

