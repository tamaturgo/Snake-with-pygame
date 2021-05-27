import pygame
import time
import random

pygame.init()
game_cycle = True
screen = pygame.display.set_mode((800, 800))
screen_bg = pygame.image.load("assets/game_screen.png")

player = pygame.image.load("assets/head_bottom.png")
player_head_x = 52 + 32
player_head_y = 52 + 32
player_dx = 0
player_dy = 32

point = pygame.image.load("assets/apple.png")
point_x = -50
point_y = -50
point_spawned = False
last_key = 0  # 0 - Down, 1 - Right, 2 - Top, 3 - Left

while game_cycle:
    if not point_spawned:
        point_x = 52 + random.randint(0, 21) * 32
        point_y = 51 + random.randint(0, 21) * 32
        point_spawned = True

    # Player Collider with wall
    player_head_x += player_dx
    player_head_y += player_dy
    if player_head_x < 52:
        player_head_x = 52
    if player_head_x > 724:
        player_head_x = 724
    if player_head_y < 50:
        player_head_y = 50
    if player_head_y > 724:
        player_head_y = 724

    player_xy = (player_head_x, player_head_y)
    point_xy = (point_x, point_y)
    screen.blit(screen_bg, (0, 0))
    screen.blit(player, player_xy)
    screen.blit(point, point_xy)

    pygame.display.flip()

    # KeyBoard Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_cycle = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_cycle = False
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and not (last_key == 2):
                player_dy = 32
                player_dx = 0
                last_key = 0
                player = pygame.image.load("assets/head_bottom.png")

            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and not(last_key == 3):
                player_dy = 0
                player_dx = 32
                last_key = 1
                player = pygame.image.load("assets/head_right.png")

            if (event.key == pygame.K_UP or event.key == pygame.K_w) and not(last_key == 0):
                player_dy = -32
                player_dx = 0
                last_key = 2
                player = pygame.image.load("assets/head_top.png")

            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and not(last_key == 1):
                player_dy = 0
                player_dx = -32
                last_key = 3
                player = pygame.image.load("assets/head_left.png")

    time.sleep(1 / 8)

pygame.quit()
