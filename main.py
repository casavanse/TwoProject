import soldier
import game_field
import pygame
import consts
import screen

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


def handle_user_events():
    global direction
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

main()