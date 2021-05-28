import pygame
import time
import random

green = (0, 155, 0)
pygame.init()
game_cycle = True
screen = pygame.display.set_mode((800, 800))
screen_bg = pygame.image.load("assets/game_screen.png")


def snake(size, list):
    for posx_y in list:
        pygame.draw.rect(screen, (255, 255, 255), [posx_y[0], posx_y[1], 32, 32])


point = pygame.image.load("assets/apple.png")
point_x = -50
point_y = -50
point_spawned = False
last_key = 0  # 0 - Down, 1 - Right, 2 - Top, 3 - Left

pos_x = 52
pos_y = 52
speed_x = 32
speed_y = 0
list_snake = []
snake_size = 1
snake_head = [pos_x, pos_y]
list_snake.append(snake_head)

while game_cycle:
    if not point_spawned:
        point_x = 52 + random.randint(0, 21) * 32
        point_y = 51 + random.randint(0, 21) * 32
        point_spawned = True

    screen.blit(screen_bg, (0, 0))
    screen.blit(point, (point_x, point_y))

    pygame.display.flip()

    # KeyBoard Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_cycle = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_cycle = False
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and not (last_key == 2):
                speed_y = 32
                speed_x = 0
                last_key = 0
                snake_size += 1
                player = pygame.image.load("assets/head_bottom.png")

            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and not (last_key == 3):
                speed_y = 0
                speed_x = 32
                last_key = 1
                snake_size += 1
                player = pygame.image.load("assets/head_right.png")

            if (event.key == pygame.K_UP or event.key == pygame.K_w) and not (last_key == 0):
                speed_y = -32
                speed_x = 0
                last_key = 2
                snake_size += 1
                player = pygame.image.load("assets/head_top.png")

            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and not (last_key == 1):
                speed_y = 0
                speed_x = -32
                last_key = 3
                snake_size += 1
                list_snake.append(snake_head)
                player = pygame.image.load("assets/head_left.png")

    pos_x += speed_x
    pos_y += speed_y

    snake_head = [pos_x, pos_y]

    list_snake.append(snake_head)

    if len(list_snake) > snake_size:
        del list_snake[0]

    snake(snake_size, list_snake)

    pygame.display.update()

    time.sleep(1 / 8)

pygame.quit()
