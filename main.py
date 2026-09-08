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
    while True:
        handle_user_events()
        soldier.move(direction)
        legs=soldier.get_soldier_feet()
        body=soldier.get_soldier_body()
        if game_field.hit_mine(legs):
           screen.lose_message()
        if game_field.hit_flag(body):
            screen.win_message()

        direction = consts.DIDNT_MOVE


def handle_user_events():
    global direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.key == pygame.K_LEFT:
            direction = consts.LEFT
        if event.key == pygame.K_RIGHT:
            direction = consts.RIGHT
        if event.key == pygame.K_UP:
            direction = consts.UP
        if event.key == pygame.K_DOWN:
            direction = consts.DOWN
        if event.key == pygame.K_RETURN:
            game_field.draw_mines()
