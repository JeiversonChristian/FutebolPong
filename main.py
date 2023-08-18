import pygame

pygame.init()

window = pygame.display.set_mode([1360,700])
title = pygame.display.set_caption("Futebol Pong")

field = pygame.image.load("assets/field.png")
window.blit(field, (0,0))

player1 = pygame.image.load("assets/player1.png")
window.blit(player1, (50, 280))

player2 = pygame.image.load("assets/player2.png")
window.blit(player2, (1235, 280))

ball = pygame.image.load("assets/ball.png")
window.blit(ball, (657, 327))

loop = True
while loop == True:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    pygame.display.update()
