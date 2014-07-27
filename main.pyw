#! python3
import pygame
import os 
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.display.set_caption('Reversi 2014')
icon = pygame.image.load('reversi-icon.png')
pygame.display.set_icon(icon)

from common import *
import menu
import reversi
import rules

# size = width, height = 1280, 800 # screen size
background = white

# panel_colour = 253,253,253

if fullscreen:
    # info = pygame.display.Info()
    # size = info.current_w,info.current_h
    screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode(size)

# in_menu = True
# in_reversi = False
mode = {'menu':True, 'reversi':False, 'rules':False, 'settings':False}

#board_reversi = pygame.image.load("board_reversi.png").convert()
#board_reversi_rect = ((100,50),board_reversi.get_size())

# r0 = reversiGame()

# import pdb; pdb.set_trace() # breakpoint - launches Python debugger
# # note: only works when terminal open

running = True
while running:
    event = pygame.event.wait() # on click
    if event.type == pygame.QUIT:
        running = False
        # sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # left click only
        if mode['menu']:
            running = menu.clickCheck(event.pos, mode)
            r0 = reversi.game() # i.e. new game
        elif mode['reversi']:
            reversi.clickCheck(event.pos, mode, reversi.spaces, r0)
        elif mode['rules']:
            rules.clickCheck(event.pos, mode)
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(str(event.button)) # testing mouse buttons
        #        left = 1
        #      middle = 2
        #       right = 3
        #   scroll up = 4
        # scroll down = 5
    if event.type == pygame.MOUSEMOTION:
        # if mode['menu']:
        #     asdf
        if mode['reversi']:
            reversi.mouseCheck(event.pos,r0)
        elif mode['menu']:
            menu.mouseCheck(event.pos)
        elif mode['rules']:
            rules.mouseCheck(event.pos)

    screen.fill(background)
    #screen.blit(board_reversi, board_reversi_rect)

    # if in_menu:
    #     menu.menuRender(screen)
    # elif in_reversi:
    #     reversi.boardRender(screen)

    if mode['menu']:
        menu.menuRender(screen)
    elif mode['reversi']:
        reversi.boardRender(screen, r0)
    elif mode['rules']:
        rules.rulesRender(screen)

    pygame.display.flip()
    #pygame.time.delay(10) #delays by 1/100 of a second to slow down movement

pygame.quit()