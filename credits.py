from constants import *


def show_center_text_screen_credits(screen, text, center_p):
    """Show text on center of screen credits"""
    initial_credits_text = game_girl_20.render(text, True, COLOR_WHITE)
    initial_credits_text_rect = initial_credits_text.get_rect()
    initial_credits_text_rect.center = center_p
    screen.blit(initial_credits_text, initial_credits_text_rect)


def show_center_text_screen_credits_size_14(screen, text, center_p):
    """Show text on center of screen credits"""
    initial_credits_text = game_girl_14.render(text, True, COLOR_WHITE)
    initial_credits_text_rect = initial_credits_text.get_rect()
    initial_credits_text_rect.center = center_p
    screen.blit(initial_credits_text, initial_credits_text_rect)


def show_left_text_screen_credits(screen, text, xy_p):
    """Show text on right of screen credits"""
    initial_credits_text = game_girl_20.render(text, True, COLOR_WHITE)
    initial_credits_text_rect = xy_p
    screen.blit(initial_credits_text, initial_credits_text_rect)


def show_all_text_on_text_scree(screen):
    """Show text on screen credits"""
    screen_bg = pygame.image.load("assets/images/diogeles.tamaturgo_credits_screen.png")
    screen.blit(screen_bg, (0, 0))

    show_center_text_screen_credits(screen, text="CREDITS", center_p=(250, 150))

    # Sounds Credits
    show_center_text_screen_credits(screen, text="SOUNDS", center_p=(250, 250))
    show_left_text_screen_credits(screen, text="Menu Music \n By mvrasseli", xy_p=(120, 270))
    show_left_text_screen_credits(screen, text="Game Music\n By Frankum\n", xy_p=(120, 290))
    show_left_text_screen_credits(screen, text="Death Sound\n By harrietniamh", xy_p=(120, 310))
    show_left_text_screen_credits(screen, text="Eating Sound\n By InspectorJ", xy_p=(120, 330))

    # Developers
    show_center_text_screen_credits(screen, text="developers", center_p=(250, 410))
    show_left_text_screen_credits(screen, text="Dayvson Silva", xy_p=(120, 430))
    show_left_text_screen_credits(screen, text="Diogeles Tamaturgo", xy_p=(120, 450))
    show_left_text_screen_credits(screen, text="Elikson Bastos", xy_p=(120, 470))
    show_left_text_screen_credits(screen, text="Lais Dib", xy_p=(120, 490))
    show_left_text_screen_credits(screen, text="Leandro Santiago", xy_p=(120, 510))

    # Credits Fonts
    show_center_text_screen_credits(screen, text="fonts", center_p=(250, 600))
    show_left_text_screen_credits(screen, text="Game_Girl by Freaky Fonts", xy_p=(120, 620))
    show_left_text_screen_credits(screen, text="Fiips by pheist", xy_p=(120, 640))

    # Return message
    show_center_text_screen_credits_size_14(screen, text="Click Anywhere to return to menu", center_p=(400, 690))
