import pygame
pygame.init()

size = width, height = 1280, 800 # screen size
black = 0, 0, 0

screen = pygame.display.set_mode(size)

speed = [1,1]

button_play = pygame.image.load("button_play.png").convert()
button_play_rect = button_play.get_rect()

while 1: #infinite loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    button_play_rect = button_play_rect.move(speed)
    if button_play_rect.left < 0 or button_play_rect.right > width:
        speed[0] = -speed[0]
    if button_play_rect.top < 0 or button_play_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(button_play, button_play_rect)
    pygame.display.flip()

    pygame.time.delay(10) #delays by 1/100 of a second to slow down movement