import pygame
import time
import apple

# Score Hud
trophy = pygame.image.load("assets/images/shiny_trophy.png")
trophy_pos = [740, 0]
apple_catch_pos = [50, 0]
# Game Variables
pygame.init()
game_cycle = True
screen = pygame.display.set_mode((800, 800))
screen_bg = pygame.image.load("assets/images/game_screen.png")
# Apple Controller
point = pygame.image.load("assets/images/apple.png")
point_pos_xy = [-100, -100]
point_spawned = False
last_key = 1  # 0 - Down, 1 - Right, 2 - Top, 3 - Left
# Snake Controller
pos_x = 52 + 64
pos_y = 52 + 32
speed_x = 32
speed_y = 0
list_snake = []
snake_size = 1
snake_head = [pos_x, pos_y]
tail = [52, 52+32]
list_snake.append(tail)
tail = [52+32, 52 + 32]
list_snake.append(tail)
list_snake.append(snake_head)
list_sprites = [[pygame.image.load("assets/images/snake_body.png"), 1],
                [pygame.image.load("assets/images/snake_body.png"), 1],
                [pygame.image.load("assets/images/head_right.png"), 1]]


def draw_snake(list_position):
    index = 0
    for pos_xy in list_position:
        if not index == 0 and not index == len(list_sprites)-1:
            list_sprites[index][0] = pygame.image.load("assets/images/snake_body.png")
        screen.blit(list_sprites[index][0], [pos_xy[0], pos_xy[1]])
        index += 1


# Game Cycle
while game_cycle:

    if not apple.apple_spawned:
        point_pos_xy = apple.spawn_apple()
        apple.apple_spawned = True

    # position next move
    pos_x += speed_x
    pos_y += speed_y

    # Snake moving
    snake_head = [pos_x, pos_y]
    list_snake.append(snake_head)

    # Removing the last block
    if len(list_snake) > snake_size:
        del list_snake[0]

    # Updating Screen
    screen.blit(screen_bg, (0, 0))
    draw_snake(list_snake)
    screen.blit(point, point_pos_xy)
    screen.blit(trophy, trophy_pos)
    screen.blit(point, apple_catch_pos)

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

            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and not (last_key == 3):
                speed_y = 0
                speed_x = 32
                last_key = 1

            if (event.key == pygame.K_UP or event.key == pygame.K_w) and not (last_key == 0):
                speed_y = -32
                speed_x = 0
                last_key = 2

            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and not (last_key == 1):
                speed_y = 0
                speed_x = -32
                last_key = 3

    # Snake collision with the side walls
    if snake_head[0] < 52 or snake_head[0] > 800 - 52:
        game_cycle = False
    if snake_head[1] < 52 or snake_head[1] > 800 - 52:
        game_cycle = False

    # Snake collision with the body
    for i in list_snake[:-1]:
        if i == snake_head:
            game_cycle = False

    # Sprite Head
    if last_key == 0:
        assets_ref = [pygame.image.load("assets/images/head_bottom.png"), 0]
    elif last_key == 1:
        assets_ref = [pygame.image.load("assets/images/head_right.png"), 1]
    elif last_key == 2:
        assets_ref = [pygame.image.load("assets/images/head_top.png"), 2]
    else:
        assets_ref = [pygame.image.load("assets/images/head_left.png"), 3]
    list_sprites[len(list_sprites) - 1] = assets_ref

    # Eating the apple and increasing the snake's body
    if snake_head[0] == point_pos_xy[0] and snake_head[1] - 1 == point_pos_xy[1]:
        snake_size += 1
        list_snake.append(snake_head)
        apple.apple_spawned = False
        list_sprites.append(assets_ref)

    pygame.display.flip()
    time.sleep(1 / 8)

pygame.quit()
