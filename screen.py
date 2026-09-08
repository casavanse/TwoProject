import random

import pygame
import consts
import game_field
import soldier

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

mine = pygame.image.load("mine.png").convert_alpha()
mine = pygame.transform.scale(mine, (consts.CELL_SIZE * 3, consts.CELL_SIZE))

soldier_img = pygame.image.load("soldier.png").convert_alpha()
soldier_img = pygame.transform.scale(soldier_img, (consts.CELL_SIZE * 2, consts.CELL_SIZE * 4))

grass_img = pygame.image.load("grass.png").convert_alpha()
grass_img = pygame.transform.scale(grass_img, (consts.CELL_SIZE * 2, consts.CELL_SIZE * 2))

flag_img = pygame.image.load("flag.png").convert_alpha()
flag_img = pygame.transform.scale(flag_img, (consts.CELL_SIZE * 4, consts.CELL_SIZE * 3))


def draw_mines():
    screen.fill(consts.BLACK)
    for row in range(0, consts.BOARD_ROWS):
        for col in range(0, consts.BOARD_COLS):
            x = consts.CELL_SIZE * col
            y = consts.CELL_SIZE * row
            rect = pygame.Rect(x, y, consts.CELL_SIZE, consts.CELL_SIZE)
            pygame.draw.rect(screen, consts.WHITE, rect, 1)
            if game_field.should_plant_mine(row, col):
                screen.blit(mine, (x, y))
    soldier_x = soldier.soldier["screen_x"]
    soldier_y = soldier.soldier["screen_y"]
    screen.blit(soldier_img, (soldier_x, soldier_y))
    pygame.display.update()
    pygame.time.wait(1000)
    draw_game()


def draw_game():
    screen.fill(consts.GREEN)
    for _ in range(consts.GRASS_COUNT):
        x, y = generate_grass()
        screen.blit(grass_img, (x, y))

    soldier_x = soldier.soldier["screen_x"]
    soldier_y = soldier.soldier["screen_y"]
    screen.blit(soldier_img, (soldier_x, soldier_y))

    flag_x = consts.WINDOW_WIDTH - consts.CELL_SIZE * 4
    flag_y = consts.WINDOW_HEIGHT - consts.CELL_SIZE * 3
    screen.blit(flag_img, (flag_x, flag_y))

    pygame.display.update()


def generate_grass():
    x_range = consts.WINDOW_WIDTH - consts.CELL_SIZE * 3
    y_range = consts.WINDOW_HEIGHT - consts.CELL_SIZE * 3
    row = random.randint(0, y_range)
    col = random.randint(0, x_range)
    return col, row

def draw_message(message, color):
    font = pygame.font.SysFont("arialblack", consts.FONT_SIZE)
    text = font.render(message, True, color)
    rect = text.get_rect(center=(consts.WINDOW_WIDTH / 2, consts.WINDOW_HEIGHT / 2))
    screen.blit(text, rect)
    pygame.display.update()

def win_message():
    draw_message(consts.WIN_MESSAGE, consts.WHITE)

def lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.BLACK)

