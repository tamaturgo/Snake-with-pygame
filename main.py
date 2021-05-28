import pygame
import time
import random

green = (0, 155, 0)
pygame.init()
game_cycle = True
screen = pygame.display.set_mode((800, 800))
screen_bg = pygame.image.load("assets/game_screen.png")


def snake(list_position):
    i = 0
    for pos_xy in list_position:
        if not i == 0 and not i == len(list_sprites)-1:
            if list_sprites[i-1][1] == 0 or list_sprites[i-1][1] == 2:
                list_sprites[i][0] = pygame.image.load("assets/snake_v.png")
            elif list_sprites[i-1][1] == 3 or list_sprites[i-1][1] == 1:
                list_sprites[i][0] = pygame.image.load("assets/snake_h.png")
                print("DIREITA OU ESQUERDA", list_sprites[i-1][1])

            for j in range(len(list_sprites), len(list_sprites)-1):
                list_sprites[j][0] = list_sprites[j-1][0]
        screen.blit(list_sprites[i][0], [pos_xy[0], pos_xy[1]])
        i += 1


point = pygame.image.load("assets/apple.png")
point_x = -50
point_y = -50
point_spawned = False
last_key = 3  # 0 - Down, 1 - Right, 2 - Top, 3 - Left

pos_x = 52 + 32
pos_y = 52
speed_x = 32
speed_y = 0
list_snake = []
snake_size = 1
snake_head = [pos_x, pos_y]
tail = [52, 52]
list_snake.append(tail)
list_snake.append(snake_head)
list_sprites = [[pygame.image.load("assets/tail_left.png"), 1],
                [pygame.image.load("assets/head_right.png"), 1]]


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
                assets_ref = [pygame.image.load("assets/head_bottom.png"), 0]
                list_sprites.append(assets_ref)
                list_snake.append(snake_head)

            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and not (last_key == 3):
                assets_ref = [pygame.image.load("assets/head_right.png"), 1]
                list_sprites.append(assets_ref)
                speed_y = 0
                speed_x = 32
                last_key = 1
                snake_size += 1
                list_snake.append(snake_head)

            if (event.key == pygame.K_UP or event.key == pygame.K_w) and not (last_key == 0):
                assets_ref = [pygame.image.load("assets/head_top.png"), 2]
                list_sprites.append(assets_ref)
                speed_y = -32
                speed_x = 0
                last_key = 2
                snake_size += 1
                list_snake.append(snake_head)

            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and not (last_key == 1):
                assets_ref = [pygame.image.load("assets/head_left.png"), 3]
                list_sprites.append(assets_ref)
                speed_y = 0
                speed_x = -32
                last_key = 3
                snake_size += 1
                list_snake.append(snake_head)

    pos_x += speed_x
    pos_y += speed_y

    snake_head = [pos_x, pos_y]

    list_snake.append(snake_head)

    if len(list_snake) > snake_size:
        del list_snake[0]

    snake(list_snake)

    pygame.display.update()

    time.sleep(1 / 8)

pygame.quit()
