import pygame
pygame.init()

class game:
    'A class for games of Reversi'

    def __init__(self):
        self.turn = 1
        self.space_states = [[0 for x in range(8)] for x in range(8)]
        self.space_states[3][4] = 1
        self.space_states[4][3] = 1
        self.space_states[3][3] = 2
        self.space_states[4][4] = 2
        self.info = "Dark plays first"
        self.infoPerm = "Dark plays first"
        # self.infoTemp = ""
        self.p1_help_on = False
        self.p2_help_on = False

    def nextTurn(self):
        self.turn += 1

    def updateInfo(self, newText):
        # self.old_info = self.info
        # self.info = newText
        self.infoPerm = newText
        self.info = self.infoPerm

    def hoverInfo(self,newText):
        self.info = newText

    def resetInfo(self):
        self.info = self.infoPerm

    def helpToggle(self):
        if self.player() == 1:
            if self.p1_help_on == True:
                self.p1_help_on = False
                self.updateInfo("Help is off for P1")
            elif self.p1_help_on == False:
                self.p1_help_on = True
                self.updateInfo("Help is on for P1")
        else:
            if self.p2_help_on == True:
                self.p2_help_on = False
                self.updateInfo("Help is off for P2")
            elif self.p2_help_on == False:
                self.p2_help_on = True
                self.updateInfo("Help is on for P2")

    def player(self):
        if self.turn % 2 == 1: # if turn is odd
            player = 1
        else:
            player = 2
        return player

    def enemy(self):
        if self.turn % 2 == 1: # if turn is odd
            enemy = 2
        else:
            enemy = 1
        return enemy

    def help_on(self):
        if self.player() == 1:
            help_on = self.p1_help_on
        else:
            help_on = self.p2_help_on
        return help_on

# if one player has no valid moves, play passes to the second player

# def currentPlayer(r0):
#     if r0.turn % 2 == 1: # if turn is odd
#         player = 1
#         enemy  = 2
#     else:
#         player = 2
#         enemy  = 1
#     return (player, enemy)

def clickCheck (click_pos, mode, spaces,r0):
    for x in range(8):
        for y in range(8):
            if spaces[x][y].collidepoint(click_pos):
                # pass x,y into moveCheck
                moveCheck(x,y,r0)
                # debugging:
                # print("clicked:", x, y)

    # if collides with buttons or other clickable things:
        # do stuff
    if button_forfeit_rect.collidepoint(click_pos):
        for m in mode:
            if m == 'menu':
                mode[m] = True
            else:
                mode[m] = False
        button_forfeit_surface.fill(panel_colour)

    if button_help_rect.collidepoint(click_pos): # if collides with help button
        # toggle
        # change toggling to a method?

        r0.helpToggle()
        # r0.updateInfo("Help is on")
        # button_help_surface.fill((200,200,200))
        # if r0.help_on == True:
        #     r0.help_on = False
        #     button_help_surface.fill(panel_colour)
        # elif r0.help_on == False:
        #     r0.help_on = True
        #     button_help_surface.fill((50,50,50))
    if r0.help_on() == False:
        button_help_surface.fill(panel_colour)
    elif r0.help_on() == True:
        button_help_surface.fill((230,230,230))
        # button_help_surface.fill((200,200,200))
        # button_help_surface.fill(helpGreen)
    return;

def spaceCheck (x,y,r0, to_flip, flip_buffer):
    # player, enemy = currentPlayer(r0)
    if r0.space_states[x][y] == r0.enemy():
        flip_buffer.append((x,y))
        done = False
    elif r0.space_states[x][y] == r0.player() and len(flip_buffer) > 0:
        to_flip.extend(flip_buffer)
        flip_buffer = []
        done = True
    else:
        flip_buffer = []
        done = True
    return done;

def moveMaker (r0, to_flip):
    # player, enemy = currentPlayer(r0)
    count = -1
    for xy in to_flip:
        x, y = xy
        r0.space_states[x][y] = r0.player()
        count += 1
    # r0.updateInfo("P" + str(player) + " took " + str(count) + " of " + "P" + str(enemy))
    # change wording?
    # r0.updateInfo("P"+str(player)+" captured "+str(count))
    if count > 1:
        r0.updateInfo("P"+str(r0.player())+" took "+str(count)+" pieces")
    else:
        r0.updateInfo("P"+str(r0.player())+" took "+str(count)+" piece")
    r0.nextTurn()
    return

def moveCheck (x,y,r0):
    xy = x, y
    to_flip = []
    flip_buffer = []

    if r0.space_states[x][y] == 0: #empty
        valid_move = True
    else:
        valid_move = False
    
    if valid_move:
        #check north
        done = False
        x, y = xy
        while y > 0 and done == False:
            y += -1
            done = spaceCheck (x,y,r0, to_flip, flip_buffer)
        flip_buffer = []
        
        #check south
        done = False
        x, y = xy
        while y < 7 and done == False:
            y += 1
            done = spaceCheck (x,y,r0, to_flip, flip_buffer)
        flip_buffer = []
        
        #check east
        done = False
        x, y = xy
        while x < 7 and done == False:
            x += 1
            done = spaceCheck (x,y,r0, to_flip, flip_buffer)
        flip_buffer = []
        
        #check west
        done = False
        x, y = xy
        while x > 0 and done == False:
            x += -1
            done = spaceCheck (x,y,r0, to_flip, flip_buffer)
        flip_buffer = []
        
        #check NE
        done = False
        x, y = xy
        while y > 0 and x < 7 and done == False:
            x += 1
            y += -1
            done = spaceCheck (x,y,r0, to_flip, flip_buffer)
        flip_buffer = []
        
        #check SE
        done = False
        x, y = xy
        while y < 7 and x < 7 and done == False:
            x += 1
            y += 1
            done = spaceCheck (x,y,r0, to_flip, flip_buffer)
        flip_buffer = []
        
        #check SW
        done = False
        x, y = xy
        while y < 7 and x > 0 and done == False:
            x += -1
            y += 1
            done = spaceCheck (x,y,r0, to_flip, flip_buffer)
        flip_buffer = []
        
        #check NW
        done = False
        x, y = xy
        while y > 0 and x > 0 and done == False:
            x += -1
            y += -1
            done = spaceCheck (x,y,r0, to_flip, flip_buffer)
        flip_buffer = []
        
        if len(to_flip) == 0:
            valid_move = False

        if valid_move:
            to_flip.append(xy)
            moveMaker(r0, to_flip)
        else:
            r0.updateInfo("Invalid move!")
    return;

def mouseCheck (mouse_pos,r0):
    # if collides with buttons or other clickable things:
        # do stuff
    if button_forfeit_rect.collidepoint(mouse_pos):
        button_forfeit_surface.fill((200,80,80))
        r0.hoverInfo("Quits to menu")
    elif button_help_rect.collidepoint(mouse_pos): # if collides with help button
        # button_help_surface.fill((230,230,230))
        button_help_surface.fill((240,240,240))
        r0.hoverInfo("Shows moves")
    else:
        r0.resetInfo()
        button_forfeit_surface.fill(panel_colour)
        if r0.help_on() == False:
            button_help_surface.fill(panel_colour)
        elif r0.help_on() == True:
            button_help_surface.fill((230,230,230))
            # button_help_surface.fill((200,200,200))
            # button_help_surface.fill(helpGreen)
    return;

def helpCheck (r0):
    for x0 in range(8):
        for y0 in range(8):
            space_help[x0][y0] = 0
            xy = x0, y0
            to_flip = []
            flip_buffer = []

            if r0.space_states[x0][y0] == 0: #empty
                valid_move = True
            else:
                valid_move = False
            
            if valid_move:
                #check north
                done = False
                x, y = xy
                while y > 0 and done == False:
                    y += -1
                    done = spaceCheck (x,y,r0, to_flip, flip_buffer)
                flip_buffer = []
                
                #check south
                done = False
                x, y = xy
                while y < 7 and done == False:
                    y += 1
                    done = spaceCheck (x,y,r0, to_flip, flip_buffer)
                flip_buffer = []
                
                #check east
                done = False
                x, y = xy
                while x < 7 and done == False:
                    x += 1
                    done = spaceCheck (x,y,r0, to_flip, flip_buffer)
                flip_buffer = []
                
                #check west
                done = False
                x, y = xy
                while x > 0 and done == False:
                    x += -1
                    done = spaceCheck (x,y,r0, to_flip, flip_buffer)
                flip_buffer = []
                
                #check NE
                done = False
                x, y = xy
                while y > 0 and x < 7 and done == False:
                    x += 1
                    y += -1
                    done = spaceCheck (x,y,r0, to_flip, flip_buffer)
                flip_buffer = []
                
                #check SE
                done = False
                x, y = xy
                while y < 7 and x < 7 and done == False:
                    x += 1
                    y += 1
                    done = spaceCheck (x,y,r0, to_flip, flip_buffer)
                flip_buffer = []
                
                #check SW
                done = False
                x, y = xy
                while y < 7 and x > 0 and done == False:
                    x += -1
                    y += 1
                    done = spaceCheck (x,y,r0, to_flip, flip_buffer)
                flip_buffer = []
                
                #check NW
                done = False
                x, y = xy
                while y > 0 and x > 0 and done == False:
                    x += -1
                    y += -1
                    done = spaceCheck (x,y,r0, to_flip, flip_buffer)
                flip_buffer = []
                
                if len(to_flip) == 0:
                    valid_move = False

                if valid_move:
                    # to_flip.append(xy)
                    # turn = moveMaker(space_states, to_flip, turn)
                    space_help[x0][y0] = 1
    return;

def boardRender (screen, r0):
    for x in range(8):
        for y in range(8):
            screen.blit(space, spaces[x][y])

    score_p1 = 0
    score_p2 = 0

    empty_space_count = 0
    for x in range(8):
        for y in range(8):
            if r0.space_states[x][y] == 1:
                screen.blit(counter1, spaces[x][y])
                score_p1 += 1
            elif r0.space_states[x][y] == 2:
                screen.blit(counter2, spaces[x][y])
                score_p2 += 1
            elif r0.space_states[x][y] == 0:
                empty_space_count += 1

    # player, enemy = currentPlayer(r0)

    if empty_space_count == 0:
        # game end
        if score_p1 > score_p2:
            # end = "Player 1 Wins!"
            r0.updateInfo("Player 1 Wins!")
        elif score_p1 < score_p2:
            # end = "Player 2 Wins!"
            r0.updateInfo("Player 2 Wins!")
        elif score_p1 == score_p2:
            # end = "You both won!"
            r0.updateInfo("You both won!")

    else:
        helpCheck(r0)
        valid_move_count = 0
        for x in range(8):
            for y in range(8):
                if space_help[x][y] == 1:
                    valid_move_count += 1
                    if r0.help_on():
                        screen.blit(help_counter, spaces[x][y])
        if valid_move_count == 0:
            r0.updateInfo("No valid move for P" + str(r0.player()))
            r0.nextTurn()

    if r0.player() == 2:
        panel_move_surface.fill(light) # now it is lights move
        label_move = font_med.render("P2's Move",1,(0,0,0))
    elif r0.player() == 1:
        panel_move_surface.fill(dark) # now it is darks move
        label_move = font_med.render("P1's Move",1,(255,255,255))

    # if r0.help_on == False:
    #     button_help_surface.fill(panel_colour)
    # elif r0.help_on == True:
    #     button_help_surface.fill((50,50,50))

    label_dark = font_med.render(("P1 - "+str(score_p1)),1,(255,255,255))
    label_light = font_med.render(("P2 - "+str(score_p2)),1,(0,0,0))
    label_turn = font_small.render(("Turn " + str(turn)),1,(0,0,0))

    label_info = font_small.render(r0.info,1,(0,0,0))

    # print panels to screen
    screen.blit(panel_move_surface, panel_move_rect)
    screen.blit(panel_dark_surface, panel_dark_rect)
    screen.blit(panel_light_surface, panel_light_rect)
    screen.blit(panel_turn_surface, panel_turn_rect)
    screen.blit(button_forfeit_surface,button_forfeit_rect)
    screen.blit(button_rules_surface,button_rules_rect)
    screen.blit(button_help_surface,button_help_rect)
    screen.blit(panel_info_surface,panel_info_rect)

    # create label rects
    label_move_rect = label_move.get_rect()
    label_dark_rect = label_dark.get_rect()
    label_light_rect = label_light.get_rect()
    label_turn_rect = label_turn.get_rect()
    label_forfeit_rect = label_forfeit.get_rect()
    label_rules_rect = label_rules.get_rect()
    label_help_rect = label_help.get_rect()
    label_info_rect = label_info.get_rect()

    # center labels on panels
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

    # print labels to screen
    screen.blit(label_move,label_move_rect)
    screen.blit(label_dark,label_dark_rect)
    screen.blit(label_light,label_light_rect)
    screen.blit(label_turn,label_turn_rect)
    screen.blit(label_forfeit,label_forfeit_rect)
    screen.blit(label_rules,label_rules_rect)
    screen.blit(label_help,label_help_rect)
    screen.blit(label_info,label_info_rect)

    return;

font_small = pygame.font.Font("Quicksand-Light.ttf", 44)
font_med = pygame.font.Font("Quicksand-Light.ttf", 48)

label_forfeit = font_small.render("Forfeit",1,(0,0,0))
label_rules = font_small.render("Rules",1,(0,0,0))
label_help = font_small.render("Help",1,(0,0,0))

# info = "moo moo"

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

spaceColour = 153, 204, 153 # light green
spaceSides  = 70, 70  # 70 px by 70 px

helpGreen = (100,200,100)

space = pygame.Surface(spaceSides)
space.fill(spaceColour)

help_counter = pygame.Surface(spaceSides)
help_counter.fill(helpGreen)

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

# help_on = False