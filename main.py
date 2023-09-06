import pygame

pygame.init()

window = pygame.display.set_mode([1360,700])
title = pygame.display.set_caption("Futebol Pong")

field = pygame.image.load("assets/field.png")

player1 = pygame.image.load("assets/player1.png")
player1_x = 50
player1_y = 280
player1_moveup = False
player1_movedown = False

player2 = pygame.image.load("assets/player2.png")
player2_x = 1235
player2_y = 280

ball = pygame.image.load("assets/ball.png")
ball_x = 657
ball_y = 327
ball_dir_x = 1
ball_dir_y = 1
ball_vel = 10

def move_player():
    global player1_y

    if player1_moveup == True:
        player1_y -= 10
        if player1_y < 0:
            player1_y = 0

    if player1_movedown == True:
        player1_y += 10
        if player1_y + player1.get_height() > 700:
            player1_y = 700 - player1.get_height()


def move_player2():
     global player2_y
     player2_y = ball_y

def move_ball():
    global ball_x
    global ball_y
    global ball_dir_x
    global ball_dir_y

    if ball_x + ball.get_width() >= player2_x and ball_x < player2_x + player2.get_width()/8 :
        if ball_y + ball.get_height() >= player2_y and ball_y <= player2_y + player2.get_height():
            ball_dir_x *= -1
    
    if ball_x <= player1_x + player1.get_width() and ball_x >= player1_x + 7*player1.get_width()/8:
        if ball_y + ball.get_height() >= player1_y and ball_y <= player1_y + player2.get_height():
            ball_dir_x *= -1 

    if ball_y + ball.get_height() >= 700 or ball_y <= 0:
        ball_dir_y *= -1

    if ball_x + ball.get_width() <= 0 or ball_x >= 1360:
        ball_x = 657
        ball_y = 327
        ball_dir_x *= -1
        ball_dir_y *= -1
    
    ball_x += ball_vel*ball_dir_x
    ball_y += ball_vel*ball_dir_y

def draw():
    window.blit(field, (0,0))
    window.blit(player1, (player1_x, player1_y))
    window.blit(player2, (player2_x, player2_y))
    window.blit(ball, (ball_x, ball_y))

loop = True
while loop == True:

    for events in pygame.event.get():

        if events.type == pygame.QUIT:
            loop = False

        # keyboard (teclado)
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                player1_moveup = True
            if events.key == pygame.K_s:
                player1_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player1_moveup = False
            if events.key == pygame.K_s:
                player1_movedown = False

    draw()
    move_ball()
    move_player()
    move_player2()
    pygame.display.update()
