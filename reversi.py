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

def clickCheck (click_pos, spaces, space_states, turn, help_on):
    for x in range(8): #beginning of important part of function code
        for y in range(8):
            if spaces[x][y].collidepoint(click_pos):
                # pass x,y into moveCheck
                turn = moveCheck(x,y,space_states, turn)
                #print("ninjas", x, y) #just a thing to close the if block
    # if collides with buttons or other clickable things:
        # do stuff
    if button_help_rect.collidepoint(click_pos):
        if help_on == True:
            help_on = False
            button_help_surface.fill(panel_colour)
        elif help_on == False:
            help_on = True
            button_help_surface.fill((50,50,50))
    return turn, help_on;

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
    # if player == 1:
    #     panel_move_surface.fill(light) # now it is lights move
    #     message_move = "Player 1's Move"
    #     label_move = font_med.render(message_move,1,(0,0,0))
    # elif player == 2:
    #     panel_move_surface.fill(dark) # now it is darks move
    #     message_move = "Player 2's Move"
    #     label_move = font_med.render(message_move,1,(255,255,255))
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

def mouseCheck (mouse_pos):
    # if collides with buttons or other clickable things:
        # do stuff
    if button_forfeit_rect.collidepoint(mouse_pos):
        button_forfeit_surface.fill((200,80,80))
    else:
        button_forfeit_surface.fill(panel_colour)
    return;

def helpCheck (space_states, turn):
    for x0 in range(8):
        for y0 in range(8):
            space_help[x0][y0] = 0
            xy = x0, y0
            to_flip = []
            flip_buffer = []

            if space_states[x0][y0] == 0: #empty
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
                    # to_flip.append(xy)
                    # turn = moveMaker(space_states, to_flip, turn)
                    space_help[x0][y0] = 1
    return;

def boardRender (screen, turn, help_on):
    for x in range(8):
        for y in range(8):
            screen.blit(space, spaces[x][y])

    score_p1 = 0
    score_p2 = 0

    empty_space_count = 0
    for x in range(8):
        for y in range(8):
            if space_states[x][y] == 1:
                screen.blit(counter1, spaces[x][y])
                score_p1 += 1
            elif space_states[x][y] == 2:
                screen.blit(counter2, spaces[x][y])
                score_p2 += 1
            elif space_states[x][y] == 0:
                empty_space_count += 1

    if empty_space_count == 0:
        # game end
        if score_p1 > score_p2:
            end = "Player 1 Wins!"
        elif score_p1 < score_p2:
            end = "Player 2 Wins!"
        elif score_p1 == score_p2:
            end = "You both won!"
    else:
        helpCheck(space_states,turn)
        valid_move_count = 0
        for x in range(8):
            for y in range(8):
                if space_help[x][y] == 1:
                    valid_move_count += 1
                    if help_on:
                        screen.blit(help_counter, spaces[x][y])
        if valid_move_count == 0:
            # no valid moves
            # show this on info panel
            # wait a few seconds
            turn += 1

    player, enemy = currentPlayer(turn)
    if player == 2:
        panel_move_surface.fill(light) # now it is lights move
        label_move = font_med.render("P2's Move",1,(0,0,0))
    elif player == 1:
        panel_move_surface.fill(dark) # now it is darks move
        label_move = font_med.render("P1's Move",1,(255,255,255))

    label_dark = font_med.render(("P1 - "+str(score_p1)),1,(255,255,255))
    label_light = font_med.render(("P2 - "+str(score_p2)),1,(0,0,0))
    label_turn = font_small.render(("Turn " + str(turn)),1,(0,0,0))

    screen.blit(panel_move_surface, panel_move_rect)
    screen.blit(panel_dark_surface, panel_dark_rect)
    screen.blit(panel_light_surface, panel_light_rect)
    screen.blit(panel_turn_surface, panel_turn_rect)
    screen.blit(button_forfeit_surface,button_forfeit_rect)
    screen.blit(button_rules_surface,button_rules_rect)
    screen.blit(button_help_surface,button_help_rect)
    screen.blit(panel_info_surface,panel_info_rect)

    label_move_rect = label_move.get_rect()
    label_dark_rect = label_dark.get_rect()
    label_light_rect = label_light.get_rect()
    label_turn_rect = label_turn.get_rect()
    label_forfeit_rect = label_forfeit.get_rect()
    label_rules_rect = label_rules.get_rect()
    label_help_rect = label_help.get_rect()
    label_info_rect = label_info.get_rect()

    label_move_rect.center = panel_move_rect.center
    label_dark_rect.center = panel_dark_rect.center
    label_light_rect.center = panel_light_rect.center
    label_turn_rect.center = panel_turn_rect.center
    label_forfeit_rect.center = button_forfeit_rect.center
    label_rules_rect.center = button_rules_rect.center
    label_help_rect.center = button_help_rect.center
    label_info_rect.center = panel_info_rect.center

    # screen.blit(label_move,panel_move_rect)
    # screen.blit(label_dark,panel_dark_rect)
    # screen.blit(label_light,panel_light_rect)
    # screen.blit(label_turn,panel_turn_rect)
    # screen.blit(label_forfeit,button_forfeit_rect)
    # screen.blit(label_rules,button_rules_rect)
    # screen.blit(label_help,button_help_rect)
    # screen.blit(label_info,panel_info_rect)

    screen.blit(label_move,label_move_rect)
    screen.blit(label_dark,label_dark_rect)
    screen.blit(label_light,label_light_rect)
    screen.blit(label_turn,label_turn_rect)
    screen.blit(label_forfeit,label_forfeit_rect)
    screen.blit(label_rules,label_rules_rect)
    screen.blit(label_help,label_help_rect)
    screen.blit(label_info,label_info_rect)

    return turn;

font_small = pygame.font.Font("Quicksand-Light.ttf", 44)
font_med = pygame.font.Font("Quicksand-Light.ttf", 48)

label_forfeit = font_small.render("Forfeit",1,(0,0,0))
label_rules = font_small.render("Rules",1,(0,0,0))
label_help = font_small.render("Help",1,(0,0,0))
label_info = font_med.render("Testing",1,(0,0,0))

# bottomEdge = height - 85

dark  = 0,0,0 # black
light = 230, 230, 230 # off-white
panel_colour = 250,250,250

panel_move_rect = pygame.Rect((785,85),(360,100))
panel_move_surface = pygame.Surface((360,100))
panel_move_surface.fill(dark)

panel_dark_rect = pygame.Rect((785,205),(170,100))
panel_dark_surface = pygame.Surface((170,100))
panel_dark_surface.fill(dark)

panel_light_rect = pygame.Rect((975,205),(170,100))
panel_light_surface = pygame.Surface((170,100))
panel_light_surface.fill(light)

panel_turn_rect = pygame.Rect((785,325),(170,100))
panel_turn_surface = pygame.Surface((170,100))
panel_turn_surface.fill(panel_colour)

button_forfeit_rect = pygame.Rect((975,325),(170,100))
button_forfeit_surface = pygame.Surface((170,100))
button_forfeit_surface.fill(panel_colour)

button_rules_rect = pygame.Rect((785,445),(170,100))
button_rules_surface = pygame.Surface((170,100))
button_rules_surface.fill(panel_colour)

button_help_rect = pygame.Rect((975,445),(170,100))
button_help_surface = pygame.Surface((170,100))
button_help_surface.fill(panel_colour)

panel_info_rect = pygame.Rect((785,565),(360,150))
panel_info_surface = pygame.Surface ((360, 150))
panel_info_surface.fill(panel_colour) 

spaceColour = 153, 204, 153
spaceSides  = 70, 70  # 70 px by 70 px

space = pygame.Surface(spaceSides)
space.fill(spaceColour)

help_counter = pygame.Surface(spaceSides)
help_counter.fill((0,100,0))

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

space_help = [[0 for x in range(8)] for x in range(8)]

turn = 1

help_on = False