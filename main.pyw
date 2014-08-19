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
import options

background = white

mode = {'menu':True, 'reversi':False, 'rules':False, 'options':False}

# debug
# import pdb; pdb.set_trace() # breakpoint - launches Python debugger
# note: only works when terminal open

running = True
while running:
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        # if quit
        running = False
        # sys.exit()
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        # if left mouse button clicked
        if mode['menu']:
            running = menu.clickCheck(event.pos, mode)
            r0 = reversi.game() # i.e. new game
        elif mode['reversi']:
            reversi.clickCheck(event.pos, mode, reversi.spaces, r0)
        elif mode['rules']:
            rules.clickCheck(event.pos, mode)
        elif mode['options']:
            options.clickCheck(event.pos, mode, config)
    if event.type == pygame.MOUSEMOTION:
        # if mouse moved
        if mode['reversi']:
            reversi.mouseCheck(event.pos,r0)
        elif mode['menu']:
            menu.mouseCheck(event.pos)
        elif mode['rules']:
            rules.mouseCheck(event.pos)
        elif mode['options']:
            options.mouseCheck(event.pos, highlight_alpha)
    # Resizing not ready for release
    # if event.type == pygame.VIDEORESIZE:
    # # if window being resized
    #     size = width, height = event.size
    #     # if width < 600:
    #     #     width = 600
    #     # if height < 400:
    #     #     height = 400
    #     screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    screen.fill(background)

    # Render screen
    if mode['menu']:
        menu.menuRender()
    elif mode['reversi']:
        reversi.boardRender(screen, r0, dark, light, space_colour)
    elif mode['rules']:
        rules.rulesRender(screen)
    elif mode['options']:
        options.optionsRender(screen, dark, light, space_colour, fullscreen)

    pygame.display.flip()

pygame.quit()