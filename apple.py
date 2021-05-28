import random

apple_spawned = False


def spawn_apple():
    point_x = 52 + random.randint(0, 21) * 32
    point_y = 51 + random.randint(0, 21) * 32
    xy = [point_x, point_y]
    return xy


