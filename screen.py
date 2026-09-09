import random
import pygame
import consts
import game_field
import soldier
import guard
import teleport

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

mine = pygame.image.load("mine.png").convert_alpha()
mine = pygame.transform.scale(mine, (consts.CELL_SIZE * 3, consts.CELL_SIZE))

soldier_img = pygame.image.load("soldier.png").convert_alpha()
soldier_img = pygame.transform.scale(soldier_img, (consts.CELL_SIZE * 2, consts.CELL_SIZE * 4))

grass_img = pygame.image.load("grass.png").convert_alpha()
grass_img = pygame.transform.scale(grass_img, (consts.CELL_SIZE * 2, consts.CELL_SIZE * 2))

flag_img = pygame.image.load("flag.png").convert_alpha()
flag_img = pygame.transform.scale(flag_img, (consts.CELL_SIZE * 4, consts.CELL_SIZE * 3))

guard_img = pygame.image.load("snake.png").convert_alpha()
guard_img = pygame.transform.scale(guard_img, (consts.CELL_SIZE * 2, consts.CELL_SIZE * 4))

teleport_img = pygame.image.load("teleport.png").convert_alpha()
teleport_img = pygame.transform.scale(mine, (consts.CELL_SIZE * 3, consts.CELL_SIZE))

grasses = []


def draw_mines():
    screen.fill(consts.BLACK)
    for row in range(0, consts.BOARD_ROWS):
        for col in range(0, consts.BOARD_COLS):
            x = consts.CELL_SIZE * col
            y = consts.CELL_SIZE * row
            rect = pygame.Rect(x, y, consts.CELL_SIZE, consts.CELL_SIZE)
            pygame.draw.rect(screen, consts.WHITE, rect, 1)
            if game_field.should_draw_mine(row, col):
                screen.blit(mine, (x, y))
            if game_field.should_draw_teleport(row, col):
                screen.blit(teleport_img, (x, y))


    soldier_x = soldier.soldier["screen_x"]
    soldier_y = soldier.soldier["screen_y"]
    screen.blit(soldier_img, (soldier_x, soldier_y))
    pygame.display.update()
    pygame.time.wait(1000)



def draw_game():
    screen.fill(consts.GREEN)

    if len(grasses) == 0:
        generate_grass()

    for x, y in grasses:
        screen.blit(grass_img, (x, y))

    soldier_x = soldier.soldier["screen_x"]
    soldier_y = soldier.soldier["screen_y"]
    screen.blit(soldier_img, (soldier_x, soldier_y))

    guard_x = guard.guard["screen_x"]
    guard_y = guard.guard["screen_y"]
    screen.blit(guard_img, (guard_x, guard_y))

    flag_x = consts.WINDOW_WIDTH - consts.CELL_SIZE * 4
    flag_y = consts.WINDOW_HEIGHT - consts.CELL_SIZE * 3
    screen.blit(flag_img, (flag_x, flag_y))

    pygame.display.update()


def generate_grass():
    global grasses
    for _ in range(consts.GRASS_COUNT):
        x_range = consts.WINDOW_WIDTH - consts.CELL_SIZE * 2
        y_range = consts.WINDOW_HEIGHT - consts.CELL_SIZE * 2
        row = random.randint(0, y_range)
        col = random.randint(0, x_range)
        grasses.append((col, row))

def draw_message(message, color):
    font = pygame.font.SysFont("arialblack", consts.FONT_SIZE)
    text = font.render(message, True, color)
    rect = text.get_rect(center=(consts.WINDOW_WIDTH / 2, consts.WINDOW_HEIGHT / 2))
    screen.blit(text, rect)
    pygame.display.update()
    pygame.time.wait(3000)

def win_message():
    draw_message(consts.WIN_MESSAGE, consts.WHITE)

def lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.BLACK)

