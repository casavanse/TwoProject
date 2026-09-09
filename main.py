# Yael Ilan and Noam Shmuely
# 331477455
# 331641753

import soldier
import game_field
import pygame
import consts
import screen
import time
import database

start = 0
soldier.create_soldier()
game_field.create()
direction = (0, 0)

pygame.init()


def main():
    global direction
    screen.draw_game()
    while True:
        handle_user_events()
        legs = soldier.get_soldier_feet()
        body = soldier.get_soldier_body()

        if game_field.hit_mine(legs):
            screen.lose_message()
            pygame.quit()
            return

        if game_field.hit_flag(body):
            screen.win_message()
            pygame.quit()
            return

        direction = consts.DIDNT_MOVE
        screen.draw_game()


def save(index):
    grid_save = game_field.add_soldier_to_grid()
    database.save(grid_save, index)


def load(index):
    new_grid = database.load(index)
    if new_grid is None:
        return
    game_field.remove_soldier_from_grid(new_grid)


def handle_user_events():
    global direction
    global start

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                direction = consts.LEFT
                soldier.move(direction)

            if event.key == pygame.K_RIGHT:
                direction = consts.RIGHT
                soldier.move(direction)

            if event.key == pygame.K_UP:
                direction = consts.UP
                soldier.move(direction)

            if event.key == pygame.K_DOWN:
                direction = consts.DOWN
                soldier.move(direction)

            if event.key == pygame.K_RETURN:
                screen.draw_mines()
                pygame.event.clear()

            if event.key in consts.KEYS_DICT.keys():
                start = time.time()

        if event.type == pygame.KEYUP:
            if event.key in consts.KEYS_DICT.keys():
                end = time.time()
                duration = end - start
                if duration <= consts.ONE_SECOND:
                    save(consts.KEYS_DICT[event.key])
                else:
                    load(consts.KEYS_DICT[event.key])


if __name__ == "__main__":
    main()
