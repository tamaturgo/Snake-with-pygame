import random
import time
import pygame

import apple
import persistence
from constants import COLOR_WHITE
from constants import game_girl_42, game_girl_20, game_girl_32
from credits import show_all_text_on_text_scree

pygame.mixer.init()
# https://freesound.org/people/mvrasseli/sounds/553495/
pygame.mixer.music.load("assets/sounds/menu_music.wav")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
# https://freesound.org/people/harrietniamh/sounds/415079/
death = pygame.mixer.Sound("assets/sounds/death_sound.wav")
death.set_volume(0.5)
# https://freesound.org/people/InspectorJ/sounds/412068/
eat = pygame.mixer.Sound("assets/sounds/eating.wav")
eat.set_volume(0.5)

# Game Variables
pygame.init()
game_cycle = True
screen = pygame.display.set_mode((800, 800))
screen_bg = pygame.image.load("assets/images/diogeles.tamaturgo_game_screen.png")
score = 0
record = 0
menu_controller = True
game_controller = False
credits_controller = False
game_over = False

# Score Hud
trophy = pygame.image.load("assets/images/lais.dib_shiny_trophy.png")
trophy_pos = [740, 0]
apple_catch_pos = [50, 0]

# Apple Controller
point = pygame.image.load("assets/images/lais.dib_apple.png")
point_pos_xy = [-100, -100]
point_spawned = False
last_key = 1  # 0 - Down, 1 - Right, 2 - Top, 3 - Left

# Snake Controller
pos_x = 52 + 64
pos_y = 52 + 32
speed_x = 32
speed_y = 0
apple_value = 1
snake_size = 1
list_snake = []
list_sprites = []


def show_text_on_credit_screen():
    """Show text on screen credits"""
    global screen_bg, event, game_cycle, menu_controller, credits_controller
    show_all_text_on_text_scree(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_cycle = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            menu_controller = True
            credits_controller = False


def menu_control():
    """Controls of menu"""
    global screen_bg, event, menu_controller, game_controller, credits_controller, game_cycle
    screen_bg = pygame.image.load("assets/images/diogeles.tamaturgo_menu_screen.png")
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] > 158 and mouse_pos[1] > 371:
        menu_play_pressed(mouse_pos)
    if mouse_pos[0] > 158 and mouse_pos[1] > 485:
        menu_credits_press(mouse_pos)
    if mouse_pos[0] > 158 and mouse_pos[1] > 610:
        menu_quit_press(mouse_pos)
    screen.blit(screen_bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_cycle = False


def menu_quit_press(mouse_pos):
    """Quit press"""
    global screen_bg, event, game_cycle
    if mouse_pos[0] < 394 and mouse_pos[1] < 670:
        screen_bg = pygame.image.load("assets/images/diogeles.tamaturgo_quit_pressed.png")
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_cycle = False


def menu_credits_press(mouse_pos):
    """Credits press"""
    global screen_bg, event, menu_controller, credits_controller
    if mouse_pos[0] < 394 and mouse_pos[1] < 554:
        screen_bg = pygame.image.load("assets/images/diogeles.tamaturgo_credits_pressed.png")
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_controller = False
                credits_controller = True


def menu_play_pressed(mouse_pos):
    """Play press"""
    global screen_bg, event, menu_controller, game_controller
    if mouse_pos[0] < 394 and mouse_pos[1] < 451:
        screen_bg = pygame.image.load("assets/images/diogeles.tamaturgo_play_pressed.png")
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_controller = False
                game_controller = True
                pygame.mixer.music.unload()
                # https://freesound.org/people/frankum/sounds/384468/
                pygame.mixer.music.load("assets/sounds/game_music.wav")
                pygame.mixer.music.play(-1)


def handle_events_on_game():
    """Handle events on play game"""
    global event, game_cycle, speed_y, speed_x, last_key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_cycle = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_cycle = False
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s)\
                    and not (last_key == 2):
                speed_y = 32
                speed_x = 0
                last_key = 0

            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d)\
                    and not (last_key == 3):
                speed_y = 0
                speed_x = 32
                last_key = 1

            if (event.key == pygame.K_UP or event.key == pygame.K_w)\
                    and not (last_key == 0):
                speed_y = -32
                speed_x = 0
                last_key = 2

            if (event.key == pygame.K_LEFT or event.key == pygame.K_a)\
                    and not (last_key == 1):
                speed_y = 0
                speed_x = -32
                last_key = 3


def snake_collision_wall():
    """Handle collision with wall"""
    global game_over
    if 52 > snake_head[0] or snake_head[0] > 800 - 52:
        game_over = True
        death.play()
        if snake_head[0] < 52:
            snake_head[0] = 53
        else:
            snake_head[0] = 800 - 53
    if snake_head[1] < 52 or snake_head[1] > 800 - 52:
        game_over = True
        death.play()
        if snake_head[1] < 52:
            snake_head[1] = 53
        else:
            snake_head[1] = 800 - 53


def init_snake():
    global snake_head, snake_size, list_snake, list_sprites
    global pos_x, pos_y, speed_x, speed_y
    speed_x = 32
    speed_y = 0
    pos_x = 52 + 64
    pos_y = 52 + 32
    list_snake = []
    snake_size = 1
    snake_head = [pos_x, pos_y]
    tail = [52, 52+32]
    list_snake.append(tail)
    tail = [52+32, 52 + 32]
    list_snake.append(tail)
    list_snake.append(snake_head)
    list_sprites = [[pygame.image.load("assets/images/diogeles.tamaturgo_snake_body.png"), 1],
                    [pygame.image.load("assets/images/diogeles.tamaturgo_snake_body.png"), 1],
                    [pygame.image.load("assets/images/lais.dib_head_right.png"), 1]]


def draw_snake(list_position):
    index = 0
    for pos_xy in list_position:
        if not index == 0 and not index == len(list_sprites)-1:
            list_sprites[index][0] = pygame.image.load("assets/images/diogeles.tamaturgo_snake_body.png")
        screen.blit(list_sprites[index][0], [pos_xy[0], pos_xy[1]])
        index += 1


init_snake()


# Game Cycle
while game_cycle:
    if menu_controller:
        menu_control()

    if credits_controller:
        show_text_on_credit_screen()

    if game_controller:
        screen_bg = pygame.image.load("assets/images/diogeles.tamaturgo_game_screen.png")
        if not apple.apple_spawned:
            aux = random.randint(1, 10)
            if aux == 1:
                point = pygame.image.load("assets/images/lais.dib_golden_apple.png")
                apple_value = 5
            elif aux == 2:
                point = pygame.image.load("assets/images/diogeles.tamaturgo_meat.png")
                apple_value = 2
            else:
                point = pygame.image.load("assets/images/lais.dib_apple.png")
                apple_value = 1

            point_pos_xy = apple.spawn_apple()
            apple.apple_spawned = True
        if not game_over:
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
        # Score
        initial_score_text = game_girl_32.render('%03d' % score,
                                                 True, COLOR_WHITE)
        initial_score_text_rect = initial_score_text.get_rect()
        initial_score_text_rect.center = (150, 20)
        # Record
        record_score_text = game_girl_32.render('%03d' % persistence.consult_score(),
                                                True, COLOR_WHITE)
        record_score_text_rect = record_score_text.get_rect()
        record_score_text_rect.center = (670, 20)
        screen.blit(screen_bg, (0, 0))
        draw_snake(list_snake)
        screen.blit(point, point_pos_xy)
        screen.blit(trophy, trophy_pos)
        screen.blit(point, apple_catch_pos)
        screen.blit(initial_score_text, initial_score_text_rect)
        screen.blit(record_score_text, record_score_text_rect)
        if game_over:
            initial_score_text = game_girl_42.render("GAME OVER", True, COLOR_WHITE)
            initial_score_text_rect = initial_score_text.get_rect()
            initial_score_text_rect.center = (400, 300)
            screen.blit(initial_score_text, initial_score_text_rect)

            initial_score_text = game_girl_32.render("Your Score: " + '%03d' % score,
                                                     True, COLOR_WHITE)
            initial_score_text_rect = initial_score_text.get_rect()
            initial_score_text_rect.center = (400, 390)
            screen.blit(initial_score_text, initial_score_text_rect)

            record_score_text = game_girl_32.render("Best score: " + '%03d' % persistence.consult_score(),
                                                    True, COLOR_WHITE)
            record_score_text_rect = record_score_text.get_rect()
            record_score_text_rect.center = (400, 430)
            screen.blit(record_score_text, record_score_text_rect)

            initial_score_text = game_girl_20.render("Press anything to restart",
                                                     True, COLOR_WHITE)
            initial_score_text_rect = initial_score_text.get_rect()
            initial_score_text_rect.center = (400, 480)
            screen.blit(initial_score_text, initial_score_text_rect)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    menu_controller = True
                    game_controller = False
                    game_over = False
                    score = 0
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("assets/sounds/menu_music.wav")
                    pygame.mixer.music.set_volume(1)
                    pygame.mixer.music.play(-1)
                    init_snake()

        # KeyBoard Events
        handle_events_on_game()

        # Snake collision with the side walls
        snake_collision_wall()
        # Snake collision with the body
        for i in list_snake[:-1]:
            # noinspection PyUnboundLocalVariable
            if i == snake_head:
                game_over = True
                death.play()
                snake_head[0] -= 1
                snake_head[1] -= 1
        # Sprite Head
        if last_key == 0:
            assets_ref = [pygame.image.load("assets/images/lais.dib_head_bottom.png"), 0]
        elif last_key == 1:
            assets_ref = [pygame.image.load("assets/images/lais.dib_head_right.png"), 1]
        elif last_key == 2:
            assets_ref = [pygame.image.load("assets/images/lais.dib_head_top.png"), 2]
        else:
            assets_ref = [pygame.image.load("assets/images/lais.dib_head_left.png"), 3]
        list_sprites[len(list_sprites) - 1] = assets_ref
        # Eating the apple and increasing the snake's body
        if snake_head[0] == point_pos_xy[0] and snake_head[1] - 1 == point_pos_xy[1]:
            if apple_value == 2:
                snake_size += 5
                for i in range(5):
                    list_snake.append(snake_head)
                    list_sprites.append(assets_ref)
            else:
                snake_size += 1
                list_snake.append(snake_head)
                list_sprites.append(assets_ref)
            eat.play()
            score += apple_value
            apple.apple_spawned = False
            persistence.update_score(score)

    pygame.display.flip()
    time.sleep(1 / 12)

pygame.quit()
