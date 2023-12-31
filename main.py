import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Pong")
run = True
player_1 = player_2 = 0 
direction = [0,1]
angle = [0, 1, 2]

#colours
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# for the ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.5, 0.5

# for the paddles
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2)
right_paddle_vel = left_paddle_vel = 0

# modifications
left_skill = right_skill =0
left_skill_remaining = right_skill_remaining = 3

# main loop
while run:
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.9
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.9
            if i.key == pygame.K_RIGHT and right_skill_remaining > 0:
                right_skill = 1
            if i.key == pygame.K_LEFT and right_skill_remaining > 0:
                right_skill = 2 
            if i.key == pygame.K_w:
                left_paddle_vel = -0.9
            if i.key == pygame.K_s:
                left_paddle_vel = 0.9
            if i.key == pygame.K_d and left_skill_remaining > 0:
                left_skill = 1
            if i.key == pygame.K_a and left_skill_remaining > 0:
                left_skill = 2 

        if i.type == pygame.KEYUP:
            right_paddle_vel = 0
            left_paddle_vel = 0

    # ball's movement controls
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    # x wins
    if ball_x >= WIDTH - radius:
        player_1 += 1 
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
               ball_vel_y, ball_vel_x = -1.4, 0.7
            if ang == 1:
               ball_vel_y, ball_vel_x = -0.7, 0.7
            if ang == 2:
               ball_vel_y, ball_vel_x = -0.7, 1.4
        if dir == 1:
            if ang == 0:
               ball_vel_y, ball_vel_x = 1.4, 0.7
            if ang == 1:
               ball_vel_y, ball_vel_x = 0.7, 0.7
            if ang == 2:
               ball_vel_y, ball_vel_x = 0.7, 1.4
    # y wins
    if ball_x <= 0 - radius:
        player_2 += 1
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
               ball_vel_y, ball_vel_x = -1.4, 0.7
            if ang == 1:
               ball_vel_y, ball_vel_x = -0.7, 0.7
            if ang == 2:
               ball_vel_y, ball_vel_x = -0.7, 1.4
        if dir == 1:
            if ang == 0:
               ball_vel_y, ball_vel_x = 1.4, 0.7
            if ang == 1:
               ball_vel_y, ball_vel_x = 0.7, 0.7
            if ang == 2:
               ball_vel_y, ball_vel_x = 0.7, 1.4
    #paddle's movement control
    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0
    # paddle collisions
    # left paddle
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *=-1
    
    # right paddle
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            ball_vel_x *=-1

    # skills
    if left_skill == 1:
        if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
            if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                ball_x = left_paddle_x + paddle_width
                ball_vel_x *=-3.5
                left_skill = 0 
                left_skill_remaining -= 1
    elif left_skill == 2:
        left_paddle_y = ball_y
        left_skill = 0
        left_skill_remaining -= 1 
    if right_skill == 1:
        if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
            if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                ball_x = right_paddle_x
                ball_vel_x *=- 3.5
                right_skill = 0
                right_skill_remaining -= 1
    elif right_skill == 2:
        right_paddle_y = ball_y
        right_skill = 0
        right_skill_remaining -= 1
    # movement
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel
    #paddle's movement control
    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0
    
    # Score Board and skill tracking
    font = pygame.font.SysFont('callibri', 32)
    score_1 = font.render("player_1:" + str(player_1), True, WHITE)
    wn.blit(score_1, (25,25))
    score_2 = font.render("player_2:" + str(player_2), True, WHITE)
    wn.blit(score_2, (825,25))
    skill_left_1 = font.render("skills left:" + str(left_skill_remaining), True, WHITE)
    wn.blit(skill_left_1, (25,65))
    skill_left_2 = font.render("skills left:" + str(right_skill_remaining), True, WHITE)
    wn.blit(skill_left_1, (825,65))

    # OBJECTS
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    if left_skill == 1:
        pygame.draw.circle(wn, WHITE, (left_paddle_x + 10, left_paddle_y +10), 4)
    if right_skill == 1:
        pygame.draw.circle(wn, WHITE, (right_paddle_x + 10, right_paddle_y +10), 4)
    
    # end screen
    winning_font = pygame.font.SysFont('callibri', 100)
    if player_1 >= 3:
        wn.fill(BLACK)
        endscreen = winning_font.render("Player_1 won!", True, WHITE)
        wn.blit(endscreen, (200,250))

    if player_2 >= 3:
        wn.fill(BLACK)
        endscreen = winning_font.render("Player_2 won!", True, WHITE)
        wn.blit(endscreen, (200,250))
    pygame.display.update()
        