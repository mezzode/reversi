# reversi.py
# By Sean Batongbacal, 2014

import pygame
pygame.init()

from common import *

class game:
    'A class for games of Reversi'

    def __init__(self):
        # Game init
        self.turn = 1
        self.space_states = [[0 for x in range(8)] for x in range(8)]
        self.space_states[3][4] = 1
        self.space_states[4][3] = 1
        self.space_states[3][3] = 2
        self.space_states[4][4] = 2
        # Key:
        # 0 = empty
        # 1 = P1 (i.e.  dark)
        # 2 = P2 (i.e. light)
        self.info = "Dark plays first" # Currently displayed info
        self.infoPerm = "Dark plays first" # Persistent info
        self.p1_help_on = False
        self.p2_help_on = False
        self.consecutive_skips = 0

    def nextTurn(self):
        self.turn += 1

    def updateInfo(self, newText):
        # Update infobox with permanent newText
        self.infoPerm = newText
        self.info = self.infoPerm

    def hoverInfo(self,newText):
        # Update infobox with temporary newText
        self.info = newText

    def resetInfo(self):
        # Reset infobox to permanent text
        self.info = self.infoPerm

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

    def helpToggle(self):
        if self.player() == 1:
            if self.p1_help_on == True:
                self.p1_help_on = False
                self.updateInfo("Hint is off for P1")
                self.hoverInfo("Show moves")
            elif self.p1_help_on == False:
                self.p1_help_on = True
                self.updateInfo("Hint is on for P1")
                self.hoverInfo("Hide moves")
        else:
            if self.p2_help_on == True:
                self.p2_help_on = False
                self.updateInfo("Hint is off for P2")
                self.hoverInfo("Show moves")
            elif self.p2_help_on == False:
                self.p2_help_on = True
                self.updateInfo("Hint is on for P2")
                self.hoverInfo("Hide moves")

    def help_on(self):
        if self.player() == 1:
            help_on = self.p1_help_on
        else:
            help_on = self.p2_help_on
        return help_on

def clickCheck (click_pos, mode, spaces,r0):
    # Determines what should be done in response to a mouse click

    # if collides with a space
    for x in range(8):
        for y in range(8):
            if spaces[x][y].collidepoint(click_pos):
                moveCheck(x,y,r0)

    # Template:
    # if collides with buttons or other clickable things:
        # do stuff
    if button_forfeit_rect.collidepoint(click_pos):
        # if collides with forfeit button
        for m in mode:
            if m == 'menu':
                mode[m] = True
            else:
                mode[m] = False
        button_forfeit_surface.fill(panel_colour)

    if button_rules_rect.collidepoint(click_pos):
        # if collides with rules button
        for m in mode:
            if m == 'rules':
                mode[m] = True
            else:
                mode[m] = False
        button_rules_surface.fill(panel_colour)

    if button_help_rect.collidepoint(click_pos):
        # if collides with help button
        r0.helpToggle()

    # Colours help button accordingly
    if r0.help_on() == False:
        button_help_surface.fill(panel_colour)
    elif r0.help_on() == True:
        button_help_surface.fill(light)
    return

def moveCheck (x,y,r0):
    # Checks whether a move is valid

    xy = x, y
    to_flip = []
    flip_buffer = []

    if r0.space_states[x][y] == 0: # empty
        valid_move = True
    else:
        valid_move = False

    if valid_move:
        # check north
        done = False
        x, y = xy
        while y > 0 and done == False:
            y += -1
            done = spaceCheck (x,y,r0, to_flip, flip_buffer)
        flip_buffer = []

        # check south
        done = False
        x, y = xy
        while y < 7 and done == False:
            y += 1
            done = spaceCheck (x,y,r0, to_flip, flip_buffer)
        flip_buffer = []

        # check east
        done = False
        x, y = xy
        while x < 7 and done == False:
            x += 1
            done = spaceCheck (x,y,r0, to_flip, flip_buffer)
        flip_buffer = []

        # check west
        done = False
        x, y = xy
        while x > 0 and done == False:
            x += -1
            done = spaceCheck (x,y,r0, to_flip, flip_buffer)
        flip_buffer = []

        # check NE
        done = False
        x, y = xy
        while y > 0 and x < 7 and done == False:
            x += 1
            y += -1
            done = spaceCheck (x,y,r0, to_flip, flip_buffer)
        flip_buffer = []

        # check SE
        done = False
        x, y = xy
        while y < 7 and x < 7 and done == False:
            x += 1
            y += 1
            done = spaceCheck (x,y,r0, to_flip, flip_buffer)
        flip_buffer = []

        # check SW
        done = False
        x, y = xy
        while y < 7 and x > 0 and done == False:
            x += -1
            y += 1
            done = spaceCheck (x,y,r0, to_flip, flip_buffer)
        flip_buffer = []

        # check NW
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
    return

def spaceCheck (x,y,r0, to_flip, flip_buffer):
    # Checks if a space should be flipped
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
    return done

def moveMaker (r0, to_flip):
    # Makes a move i.e. places and flips pieces

    # Flips pieces
    count = -1
    for xy in to_flip:
        print(str(xy)) # from stub
        x, y = xy
        r0.space_states[x][y] = r0.player()
        count += 1

    # Displays how many pieces were flipped
    if count > 1:
        r0.updateInfo("P"+str(r0.player())+" took "+str(count)+" pieces")
    else:
        r0.updateInfo("P"+str(r0.player())+" took "+str(count)+" piece")
    r0.nextTurn()
    return

def mouseCheck (mouse_pos,r0):
    # Determines what should be done in response to a mouse movement

    # Template:
    # if collides with something:
        # do stuff
    if button_forfeit_rect.collidepoint(mouse_pos):
        # collides with forfeit button
        print("Highlight Forfeit") # from stub
        button_forfeit_surface.fill((quit_colour))
        r0.hoverInfo("Quits to menu")
    elif button_rules_rect.collidepoint(mouse_pos):
        # collides with forfeit button
        print("Highlight Rules") # from stub
        button_rules_surface.fill((highlight_colour))
        r0.hoverInfo("Reversi rules")
    elif button_help_rect.collidepoint(mouse_pos):
        # collides with help button
        print("Highlight Help") # from stub
        button_help_surface.fill(highlight_colour)
        if r0.help_on():
            r0.hoverInfo("Hide moves")
        else:
            r0.hoverInfo("Show moves")
    else:
        r0.resetInfo()
        button_forfeit_surface.fill(panel_colour)
        button_rules_surface.fill(panel_colour)
        if r0.help_on() == False:
            button_help_surface.fill(panel_colour)
        elif r0.help_on() == True:
            button_help_surface.fill(light)
    return

def helpCheck (r0):
    # Determines current player's valid moves
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
                # check north
                done = False
                x, y = xy
                while y > 0 and done == False:
                    y += -1
                    done = spaceCheck (x,y,r0, to_flip, flip_buffer)
                flip_buffer = []

                # check south
                done = False
                x, y = xy
                while y < 7 and done == False:
                    y += 1
                    done = spaceCheck (x,y,r0, to_flip, flip_buffer)
                flip_buffer = []

                # check east
                done = False
                x, y = xy
                while x < 7 and done == False:
                    x += 1
                    done = spaceCheck (x,y,r0, to_flip, flip_buffer)
                flip_buffer = []

                # check west
                done = False
                x, y = xy
                while x > 0 and done == False:
                    x += -1
                    done = spaceCheck (x,y,r0, to_flip, flip_buffer)
                flip_buffer = []

                # check NE
                done = False
                x, y = xy
                while y > 0 and x < 7 and done == False:
                    x += 1
                    y += -1
                    done = spaceCheck (x,y,r0, to_flip, flip_buffer)
                flip_buffer = []

                # check SE
                done = False
                x, y = xy
                while y < 7 and x < 7 and done == False:
                    x += 1
                    y += 1
                    done = spaceCheck (x,y,r0, to_flip, flip_buffer)
                flip_buffer = []

                # check SW
                done = False
                x, y = xy
                while y < 7 and x > 0 and done == False:
                    x += -1
                    y += 1
                    done = spaceCheck (x,y,r0, to_flip, flip_buffer)
                flip_buffer = []

                # check NW
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
                    space_help[x0][y0] = 1
    return

def boardRender (screen, r0):
    # Updates non-permanent display elements

    # Display board spaces
    for x in range(8):
        for y in range(8):
            screen.blit(space, spaces[x][y])

    # Count pieces and empty spaces
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

    # Determine whether game has ended
    if empty_space_count == 0 or r0.consecutive_skips == 2:
        # Game has ended
        if score_p1 > score_p2:
            print("Player 1 Wins!") # from stub
            r0.updateInfo("Player 1 Wins!")
        elif score_p1 < score_p2:
            print("Player 2 Wins!") # from stub
            r0.updateInfo("Player 2 Wins!")
        elif score_p1 == score_p2:
            print("You both won!") # from stub
            r0.updateInfo("You both won!")
    else:
        # Game has not ended

        # Determine valid moves, highlight if help is on
        helpCheck(r0)
        valid_move_count = 0
        for x in range(8):
            for y in range(8):
                if space_help[x][y] == 1:
                    valid_move_count += 1
                    if r0.help_on():
                        screen.blit(help_counter, spaces[x][y])
        if valid_move_count == 0:
            # Current player has no valid moves, skips turn
            print("No valid move") # from stub
            r0.updateInfo("No moves for P" + str(r0.player()))
            r0.nextTurn()
            r0.consecutive_skips += 1
        else:
            # Current player has valid moves
            r0.consecutive_skips = 0

    # Set non-permanent labels
    label_dark = font_med.render(("P1 - "+str(score_p1)),1,white)
    label_light = font_med.render(("P2 - "+str(score_p2)),1,black)
    label_turn = font_small.render(("Turn " + str(r0.turn)),1,black)
    label_info = font_small.render(r0.info,1,black)
    if r0.player() == 1:
        # Dark's (i.e. P1's) Move
        panel_move_surface.fill(dark)
        label_move = font_med.render("P1's Move",1,white)
    elif r0.player() == 2:
        # Light's (i.e. P2's) Move
        panel_move_surface.fill(light)
        label_move = font_med.render("P2's Move",1,black)

    # Display panels to screen
    screen.blit(panel_move_surface, panel_move_rect)
    screen.blit(panel_dark_surface, panel_dark_rect)
    screen.blit(panel_light_surface, panel_light_rect)
    screen.blit(panel_turn_surface, panel_turn_rect)
    screen.blit(button_forfeit_surface,button_forfeit_rect)
    screen.blit(button_rules_surface,button_rules_rect)
    screen.blit(button_help_surface,button_help_rect)
    screen.blit(panel_info_surface,panel_info_rect)

    # Create label rects
    label_move_rect = label_move.get_rect()
    label_dark_rect = label_dark.get_rect()
    label_light_rect = label_light.get_rect()
    label_turn_rect = label_turn.get_rect()
    label_forfeit_rect = label_forfeit.get_rect()
    label_rules_rect = label_rules.get_rect()
    label_help_rect = label_help.get_rect()
    label_info_rect = label_info.get_rect()

    # Centre labels on panels
    label_move_rect.center = panel_move_rect.center
    label_dark_rect.center = panel_dark_rect.center
    label_light_rect.center = panel_light_rect.center
    label_turn_rect.center = panel_turn_rect.center
    label_forfeit_rect.center = button_forfeit_rect.center
    label_rules_rect.center = button_rules_rect.center
    label_help_rect.center = button_help_rect.center
    label_info_rect.center = panel_info_rect.center

    # Display labels to screen
    screen.blit(label_move,label_move_rect)
    screen.blit(label_dark,label_dark_rect)
    screen.blit(label_light,label_light_rect)
    screen.blit(label_turn,label_turn_rect)
    screen.blit(label_forfeit,label_forfeit_rect)
    screen.blit(label_rules,label_rules_rect)
    screen.blit(label_help,label_help_rect)
    screen.blit(label_info,label_info_rect)

    return

#############################
# Permanent Screen Elements #
#############################

# # Colours
# black = 0,0,0
# white = 255,255,255
# dark  = 0,0,0                  # black
# light = 230, 230, 230          # light grey
# panel_colour = 253,253,253     # off white
# space_colour = 153, 204, 153   # light green
# helpGreen = 100,200,100        # brighter green
# highlight_colour = 240,240,240 # lighter grey

# # Fonts
# font_small = pygame.font.Font("Quicksand-Light.ttf", 44)
# font_med = pygame.font.Font("Quicksand-Light.ttf", 48)

# Labels
label_forfeit = font_small.render("Quit",1,black)
label_rules = font_small.render("Rules",1,black)
label_help = font_small.render("Hint",1,black)

# P1/P2's Move Panel
panel_move_rect = pygame.Rect((785,y_buffer),(controls_width,panel_height))
panel_move_rect.top = y_buffer
panel_move_rect.left = spaces[7][0].right + controls_buffer
panel_move_surface = pygame.Surface((controls_width,panel_height))
panel_move_surface.fill(dark)

# Dark  (i.e. P1) Score Panel
panel_dark_rect = pygame.Rect((785,y_buffer+panel_height+controls_buffer),(panel_width,panel_height))
panel_dark_rect.top = panel_move_rect.bottom + controls_buffer
panel_dark_rect.left = panel_move_rect.left
panel_dark_surface = pygame.Surface((panel_width,panel_height))
panel_dark_surface.fill(dark)

# Light (i.e. P2) Score Panel
panel_light_rect = pygame.Rect((975,y_buffer+panel_height+controls_buffer),(panel_width,panel_height))
panel_light_rect.top = panel_move_rect.bottom + controls_buffer
panel_light_rect.right = panel_move_rect.right
panel_light_surface = pygame.Surface((panel_width,panel_height))
panel_light_surface.fill(light)

# Turn Counter Panel
panel_turn_rect = pygame.Rect((785,y_buffer+(panel_height+controls_buffer)*2),(panel_width,panel_height))
panel_turn_rect.top = panel_dark_rect.bottom + controls_buffer
panel_turn_rect.left = panel_dark_rect.left
panel_turn_surface = pygame.Surface((panel_width,panel_height))
panel_turn_surface.fill(panel_colour)

# Forfeit Button
button_forfeit_rect = pygame.Rect((975,y_buffer+(panel_height+controls_buffer)*2),(panel_width,panel_height))
button_forfeit_rect.top = panel_light_rect.bottom + controls_buffer
button_forfeit_rect.right = panel_light_rect.right
button_forfeit_surface = pygame.Surface((panel_width,panel_height))
button_forfeit_surface.fill(panel_colour)

# Rules Button
button_rules_rect = pygame.Rect((785,y_buffer+(panel_height+controls_buffer)*3),(panel_width,panel_height))
button_rules_rect.top = panel_turn_rect.bottom + controls_buffer
button_rules_rect.left = panel_turn_rect.left
button_rules_surface = pygame.Surface((panel_width,panel_height))
button_rules_surface.fill(panel_colour)

# Help Button
button_help_rect = pygame.Rect((975,y_buffer+(panel_height+controls_buffer)*3),(panel_width,panel_height))
button_help_rect.top = button_forfeit_rect.bottom + controls_buffer
button_help_rect.right = button_forfeit_rect.right
button_help_surface = pygame.Surface((panel_width,panel_height))
button_help_surface.fill(panel_colour)

# Info Panel (AKA Infobox)
panel_info_rect = pygame.Rect((785,y_buffer+(panel_height+controls_buffer)*4),(360,150))
panel_info_rect.top = button_rules_rect.bottom + controls_buffer
panel_info_rect.left = button_rules_rect.left
panel_info_surface = pygame.Surface ((360, 150))
panel_info_surface.fill(panel_colour)
