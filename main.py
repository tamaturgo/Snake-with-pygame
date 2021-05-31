import pygame
import time
import apple
import random
import persistence

# Sounds
pygame.mixer.init()
# https://freesound.org/people/mvrasseli/sounds/553495/
pygame.mixer.music.load("assets/sounds/553495__mvrasseli__4-4-100bpm-streets-funky-loop.wav")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
# https://freesound.org/people/harrietniamh/sounds/415079/
death = pygame.mixer.Sound("assets/sounds/death_sound.wav")
death.set_volume(0.5)
# Game Variables
pygame.init()
game_cycle = True
screen = pygame.display.set_mode((800, 750))
screen_bg = pygame.image.load("assets/images/game_screen.png")
score = 0
menu_controller = True
game_controller = False
credits_controller = False
game_over = False
# -----------------------------------------------------
# Record's Variable
record = 0
# -----------------------------------------------------

# Score Hud
trophy = pygame.image.load("assets/images/shiny_trophy.png")
trophy_pos = [740, 0]
apple_catch_pos = [50, 0]

# Fonts
game_girl_42 = pygame.font.Font('assets/fonts/game_girl_classic.ttf', 42)
game_girl_32 = pygame.font.Font('assets/fonts/game_girl_classic.ttf', 32)
game_girl_20 = pygame.font.Font('assets/fonts/game_girl_classic.ttf', 20)
game_girl_14 = pygame.font.Font('assets/fonts/game_girl_classic.ttf', 14)

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
apple_value = 1
snake_size = 1
list_snake = []
list_sprites = []


def init_snake():
    global snake_head
    global snake_size
    global list_snake
    global list_sprites
    global pos_x
    global pos_y
    global speed_x
    global speed_y
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


init_snake()

# Game Cycle
while game_cycle:
    if menu_controller:
        screen_bg = pygame.image.load("assets/images/menu_screen.png")
        mouse_pos = pygame.mouse.get_pos()

        if mouse_pos[0] > 158 and mouse_pos[1] > 371:
            if mouse_pos[0] < 394 and mouse_pos[1] < 451:
                screen_bg = pygame.image.load("assets/images/play_pressed.png")
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        menu_controller = False
                        game_controller = True
                        pygame.mixer.music.unload()
                        # https://freesound.org/people/frankum/sounds/384468/
                        pygame.mixer.music.load("assets/sounds/384468__frankum__vintage-elecro-pop-loop.mp3")
                        pygame.mixer.music.play(-1)

        if mouse_pos[0] > 158 and mouse_pos[1] > 485:
            if mouse_pos[0] < 394 and mouse_pos[1] < 554:
                screen_bg = pygame.image.load("assets/images/credits_pressed.png")
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        menu_controller = False
                        credits_controller = True

        if mouse_pos[0] > 158 and mouse_pos[1] > 610:
            if mouse_pos[0] < 394 and mouse_pos[1] < 670:
                screen_bg = pygame.image.load("assets/images/quit_pressed.png")
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        game_cycle = False

        screen.blit(screen_bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_cycle = False

    if credits_controller:
        screen_bg = pygame.image.load("assets/images/credits_screen.png")
        screen.blit(screen_bg, (0, 0))
        initial_credits_text = game_girl_32.render("CREDITS", True, (255, 255, 255))
        initial_credits_text_rect = initial_credits_text.get_rect()
        initial_credits_text_rect.center = (250, 150)
        screen.blit(initial_credits_text, initial_credits_text_rect)
        # Sounds Credits
        initial_credits_text = game_girl_20.render("SOUNDS", True, (255, 255, 255))
        initial_credits_text_rect = initial_credits_text.get_rect()
        initial_credits_text_rect.center = (250, 250)
        screen.blit(initial_credits_text, initial_credits_text_rect)
        initial_credits_text = game_girl_20.render("Menu Music \n By mvrasseli", True, (255, 255, 255))
        initial_credits_text_rect = initial_credits_text.get_rect()
        initial_credits_text_rect = (120, 270)
        screen.blit(initial_credits_text, initial_credits_text_rect)
        initial_credits_text = game_girl_20.render("Game Music\n By Frankum\n", True, (255, 255, 255))
        initial_credits_text_rect = initial_credits_text.get_rect()
        initial_credits_text_rect = (120, 290)
        screen.blit(initial_credits_text, initial_credits_text_rect)
        initial_credits_text = game_girl_20.render("Death Sound\n By harrietniamh", True, (255, 255, 255))
        initial_credits_text_rect = initial_credits_text.get_rect()
        initial_credits_text_rect = (120, 310)
        screen.blit(initial_credits_text, initial_credits_text_rect)

        # Developers
        initial_credits_text = game_girl_20.render("Developers", True, (255, 255, 255))
        initial_credits_text_rect = initial_credits_text.get_rect()
        initial_credits_text_rect.center = (250, 410)
        screen.blit(initial_credits_text, initial_credits_text_rect)
        initial_credits_text = game_girl_20.render("Dayvson Silva", True, (255, 255, 255))
        initial_credits_text_rect = initial_credits_text.get_rect()
        initial_credits_text_rect = (120, 430)
        screen.blit(initial_credits_text, initial_credits_text_rect)
        initial_credits_text = game_girl_20.render("Diogeles Tamaturgo", True, (255, 255, 255))
        initial_credits_text_rect = initial_credits_text.get_rect()
        initial_credits_text_rect = (120, 450)
        screen.blit(initial_credits_text, initial_credits_text_rect)
        initial_credits_text = game_girl_20.render("Elikson Bastos", True, (255, 255, 255))
        initial_credits_text_rect = initial_credits_text.get_rect()
        initial_credits_text_rect = (120, 470)
        screen.blit(initial_credits_text, initial_credits_text_rect)
        initial_credits_text = game_girl_20.render("Lais Dib", True, (255, 255, 255))
        initial_credits_text_rect = initial_credits_text.get_rect()
        initial_credits_text_rect = (120, 490)
        screen.blit(initial_credits_text, initial_credits_text_rect)
        initial_credits_text = game_girl_20.render("Leandro Santiago", True, (255, 255, 255))
        initial_credits_text_rect = initial_credits_text.get_rect()
        initial_credits_text_rect = (120, 510)
        screen.blit(initial_credits_text, initial_credits_text_rect)

        # Credits Fonts
        initial_credits_text = game_girl_20.render("Fonts", True, (255, 255, 255))
        initial_credits_text_rect = initial_credits_text.get_rect()
        initial_credits_text_rect.center = (250, 600)
        screen.blit(initial_credits_text, initial_credits_text_rect)
        initial_credits_text = game_girl_20.render("Game_Girl by Freaky Fonts", True, (255, 255, 255))
        initial_credits_text_rect = initial_credits_text.get_rect()
        initial_credits_text_rect = (120, 620)
        screen.blit(initial_credits_text, initial_credits_text_rect)
        initial_credits_text = game_girl_20.render("Fiips by pheist", True, (255, 255, 255))
        initial_credits_text_rect = initial_credits_text.get_rect()
        initial_credits_text_rect = (120, 640)
        screen.blit(initial_credits_text, initial_credits_text_rect)

        initial_credits_text = game_girl_14.render("Click Anywhere to return to menu", True, (255, 255, 255))
        initial_credits_text_rect = initial_credits_text.get_rect()
        initial_credits_text_rect.center = (400, 690)
        screen.blit(initial_credits_text, initial_credits_text_rect)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_cycle = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu_controller = True
                    credits_controller = False

    if game_controller:
        screen_bg = pygame.image.load("assets/images/game_screen.png")
        if not apple.apple_spawned:
            aux = random.randint(1, 10)
            if aux == 1:
                point = pygame.image.load("assets/images/golden_apple.png")
                apple_value = 5
            elif aux == 2:
                point = pygame.image.load("assets/images/meat.png")
                apple_value = 2
            else:
                point = pygame.image.load("assets/images/apple.png")
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
        initial_score_text = game_girl_32.render('%03d' % score, True, (255, 255, 255))
        initial_score_text_rect = initial_score_text.get_rect()
        initial_score_text_rect.center = (150, 20)

        # Record
        record_score_text = game_girl_32.render('%03d' % record, True, (255, 255, 255))
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
            initial_score_text = game_girl_42.render("GAME OVER", True, (255, 255, 255))
            initial_score_text_rect = initial_score_text.get_rect()
            initial_score_text_rect.center = (400, 300)
            screen.blit(initial_score_text, initial_score_text_rect)

            initial_score_text = game_girl_32.render("Your Score: " + '%03d' % score, True, (255, 255, 255))
            initial_score_text_rect = initial_score_text.get_rect()
            initial_score_text_rect.center = (400, 390)
            screen.blit(initial_score_text, initial_score_text_rect)

            record_score_text = game_girl_32.render("Best score: " + '%03d' % persistence.consult_score(), True, (255, 255, 255))
            record_score_text_rect = record_score_text.get_rect()
            record_score_text_rect.center = (400, 430)
            screen.blit(record_score_text, record_score_text_rect)

            initial_score_text = game_girl_20.render("Press anything to restart", True, (255, 255, 255))
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
                    pygame.mixer.music.load("assets/sounds/553495__mvrasseli__4-4-100bpm-streets-funky-loop.wav")
                    pygame.mixer.music.set_volume(1)
                    pygame.mixer.music.play(-1)
                    init_snake()

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
            game_over = True
            death.play()
            if snake_head[0] < 52:
                snake_head[0] = 53
            else:
                snake_head[0] = 800-53
        if snake_head[1] < 52 or snake_head[1] > 800 - 52:
            game_over = True
            death.play()
            if snake_head[1] < 52:
                snake_head[1] = 53
            else:
                snake_head[1] = 800-53

        # Snake collision with the body
        for i in list_snake[:-1]:
            if i == snake_head:
                game_over = True
                death.play()
                snake_head[0] -= 1
                snake_head[1] -= 1

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
            if apple_value == 2:
                snake_size += 5
                for i in range(5):
                    list_snake.append(snake_head)
                    list_sprites.append(assets_ref)
            else:
                snake_size += 1
                list_snake.append(snake_head)
                list_sprites.append(assets_ref)

            score += apple_value
            apple.apple_spawned = False
            persistence.update_score(score)

    pygame.display.flip()
    time.sleep(1 / 12)

pygame.quit()
