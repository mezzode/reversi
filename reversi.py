import pygame
pygame.init()

# if one player has no valid moves, play passes to the second player

def currentPlayer(turn):
    if turn % 2 == 1: # if turn is odd
        player = 1
        enemy  = 2
    else:
        player = 2
        enemy  = 1
    return (player, enemy)

def clickCheck (click_pos, spaces, space_states, turn):
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
        
        #check south
        done = False
        x, y = xy
        while y < 7 and done == False:
            y += 1
            done = spaceCheck (x,y,space_states,turn, to_flip, flip_buffer)
        flip_buffer = []
        
        #check east
        done = False
        x, y = xy
        while x < 7 and done == False:
            x += 1
            done = spaceCheck (x,y,space_states,turn, to_flip, flip_buffer)
        flip_buffer = []
        
        #check west
        done = False
        x, y = xy
        while x > 0 and done == False:
            x += -1
            done = spaceCheck (x,y,space_states,turn, to_flip, flip_buffer)
        flip_buffer = []
        
        #check NE
        done = False
        x, y = xy
        while y > 0 and x < 7 and done == False:
            x += 1
            y += -1
            done = spaceCheck (x,y,space_states,turn, to_flip, flip_buffer)
        flip_buffer = []
        
        #check SE
        done = False
        x, y = xy
        while y < 7 and x < 7 and done == False:
            x += 1
            y += 1
            done = spaceCheck (x,y,space_states,turn, to_flip, flip_buffer)
        flip_buffer = []
        
        #check SW
        done = False
        x, y = xy
        while y < 7 and x > 0 and done == False:
            x += -1
            y += 1
            done = spaceCheck (x,y,space_states,turn, to_flip, flip_buffer)
        flip_buffer = []
        
        #check NW
        done = False
        x, y = xy
        while y > 0 and x > 0 and done == False:
            x += -1
            y += -1
            done = spaceCheck (x,y,space_states,turn, to_flip, flip_buffer)
        flip_buffer = []
        
        if len(to_flip) == 0:
            valid_move = False

        if valid_move:
            to_flip.append(xy)
            turn = moveMaker(space_states, to_flip, turn)
    return turn;

def boardRender (screen):
    for x in range(8):
        for y in range(8):
            screen.blit(space, spaces[x][y])

    for x in range(8):
        for y in range(8):
            if space_states[x][y] == 1:
                screen.blit(counter1, spaces[x][y])
            elif space_states[x][y] == 2:
                screen.blit(counter2, spaces[x][y])
    return;

spaceColour = 153, 204, 153
spaceSides  = 70, 70  # 70 px by 70 px

space = pygame.Surface(spaceSides)
space.fill(spaceColour)

dark  = 0,0,0 # black
light = 230, 230, 230 # off-white

counter1 = pygame.Surface(spaceSides)
counter1.fill(dark)
counter2 = pygame.Surface(spaceSides)
counter2.fill(light)

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
turn = 1