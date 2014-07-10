import pygame
pygame.init()

def clickCheck (click_pos, mode):
    # Determines what should be done in response to a mouse click

    if button_return_rect.collidepoint(click_pos): # if return is clicked
        button_return_surface.fill(panel_colour)
        for m in mode:
            if m == 'reversi':
                mode[m] = True
                # r0 = reversiGame()
            else:
                mode[m] = False
    return

def mouseCheck (mouse_pos):
    # Determines what should be done in response to a mouse movement

    # template:
    # if mouse collides with button:
        # do stuff

    if button_return_rect.collidepoint(mouse_pos):
        button_return_surface.fill((240,240,240))
    else:
        button_return_surface.fill(panel_colour)
    return

def rulesRender(screen):
    screen.blit(button_return_surface, button_return_rect)
    # screen.blit(panel_title_surface,panel_title_rect)
    screen.blit(label_return,label_return_rect)
    screen.blit(label_title,label_title_rect)
    screen.blit(label_rules_1,label_rules_1_rect)
    screen.blit(label_rules_2,label_rules_2_rect)
    screen.blit(label_rules_3,label_rules_3_rect)
    screen.blit(label_rules_4,label_rules_4_rect)
    screen.blit(label_rules_5,label_rules_5_rect)

    screen.blit(help_counter, spaces[0][7])
    screen.blit(counter2, spaces[0][6])
    screen.blit(counter2, spaces[1][6])
    screen.blit(counter2, spaces[1][7])
    screen.blit(counter1, spaces[0][5])
    screen.blit(counter1, spaces[2][5])
    screen.blit(counter1, spaces[2][7])
    screen.blit(space, spaces[1][5])
    screen.blit(space, spaces[2][6])

    screen.blit(counter1, spaces[4][7])
    screen.blit(counter1, spaces[4][6])
    screen.blit(counter1, spaces[5][6])
    screen.blit(counter1, spaces[5][7])
    screen.blit(counter1, spaces[4][5])
    screen.blit(counter1, spaces[6][5])
    screen.blit(counter1, spaces[6][7])
    screen.blit(space, spaces[5][5])
    screen.blit(space, spaces[6][6])

size = width, height = 1280, 800 # screen size

# Colours
black = 0,0,0
white = 255,255,255
dark  = 0,0,0                  # black
light = 230, 230, 230          # light grey
panel_colour = 253,253,253     # off white
space_colour = 153, 204, 153   # light green
helpGreen = 100,200,100        # brighter green
highlight_colour = 240,240,240 # lighter grey

font_small = pygame.font.Font("Quicksand-Light.ttf", 44)
font_med = pygame.font.Font("Quicksand-Light.ttf", 48)
font_large = pygame.font.Font("Quicksand-Light.ttf", 72)
font_title = pygame.font.Font("Quicksand-Light.ttf", 100)

panel_colour = 253,253,253

panel_title_rect = pygame.Rect((135,85),(300,100))
panel_title_surface = pygame.Surface((300,100))
panel_title_surface.fill(panel_colour)

label_title = font_large.render("Rules",1,(0,0,0))
label_title_rect = label_title.get_rect()
label_title_rect.center = (width/2,225)
label_title_rect.topleft = 135,85

button_return_rect = pygame.Rect((785,615),(360,100))
button_return_surface = pygame.Surface((360,100))
button_return_surface.fill(panel_colour)

label_return = font_med.render("Back to Game",1,(0,0,0))
label_return_rect = label_return.get_rect()
# label_return_rect.left = label_title_rect.left

label_rules_1 = font_small.render("Take enemy pieces by placing one of your ",1,(0,0,0))
label_rules_2 = font_small.render("own to trap their pieces between the one you",1,(0,0,0))
label_rules_3 = font_small.render("just placed and another one of your pieces.",1,(0,0,0))
label_rules_4 = font_small.render("Whoever has the most pieces when neither ",1,(0,0,0))
label_rules_5 = font_small.render("player can make a move wins!",1,(0,0,0))
label_rules_1_rect = label_rules_1.get_rect()
label_rules_2_rect = label_rules_2.get_rect()
label_rules_3_rect = label_rules_3.get_rect()
label_rules_4_rect = label_rules_4.get_rect()
label_rules_5_rect = label_rules_5.get_rect()
label_rules_1_rect.topleft = label_title_rect.bottomleft
label_rules_1_rect.top = label_rules_1_rect.top + 20
label_rules_2_rect.topleft = label_rules_1_rect.bottomleft
label_rules_3_rect.topleft = label_rules_2_rect.bottomleft
label_rules_4_rect.topleft = label_rules_3_rect.bottomleft
label_rules_4_rect.top = label_rules_4_rect.top + 15
label_rules_5_rect.topleft = label_rules_4_rect.bottomleft

# whitespace = (height - (label_title_rect.height + button_return_rect.height))/3
whitespace = height/3
# button_return_rect.top = label_title_rect.bottom + whitespace
# label_return_rect.bottom = whitespace * 2
# label_title_rect.centery = button_return_rect.top/2
# panel_title_rect.centery = button_return_rect.top/2
# label_return_rect.centery = button_return_rect.centery
# button_return_rect.centerx = label_return_rect.centerx
# label_title_rect.center = panel_title_rect.center
label_return_rect.center = button_return_rect.center

# Spaces (i.e. Board)
space_sides  = 70, 70  # Size of each space i.e. 70 px by 70 px
space = pygame.Surface(space_sides)
space.fill(space_colour)
spaces = [[0 for x in range(8)] for x in range(8)] # Spaces Array (i.e. Board) init
for x in range(8):
    for y in range(8):
        spaces[x][y] = pygame.Rect((135 + 80 * x, 85 + 80 * y),space_sides)

# P1's and P2's Counters
counter1 = pygame.Surface(space_sides)
counter1.fill(dark)
counter2 = pygame.Surface(space_sides)
counter2.fill(light)

# Help-highlighted Spaces
help_counter = pygame.Surface(space_sides)
help_counter.fill(helpGreen)

# for x in range(8):
#     for y in range(8):
#         if r0.space_states[x][y] == 1:
#             screen.blit(counter1, spaces[x][y])
#             score_p1 += 1
#         elif r0.space_states[x][y] == 2:
#             screen.blit(counter2, spaces[x][y])
#             score_p2 += 1
#         elif r0.space_states[x][y] == 0:
#             empty_space_count += 1