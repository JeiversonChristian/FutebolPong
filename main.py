import pygame

pygame.init()

window = pygame.display.set_mode([1360,700])

title = pygame.display.set_caption("Futebol Pong")

loop = True
while loop == True:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    pygame.display.update()
