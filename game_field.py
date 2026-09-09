import pygame
import consts
import random
import soldier
import copy

grid = []
flag_row = consts.BOARD_ROWS - consts.FLAG_ROWS
flag_col = consts.BOARD_COLS - consts.FLAG_COLS
start_position = [(0, 0), (0, 1),
                  (1, 0), (1, 1),
                  (2, 0), (2, 1),
                  (3, 0), (3, 1)]


def create():
    global grid
    grid = [[consts.EMPTY_CELL for _ in range(consts.BOARD_COLS)] for _ in range(consts.BOARD_ROWS)]
    for row in range(consts.FLAG_ROWS):
        for col in range(consts.FLAG_COLS):
            grid[row + flag_row][col + flag_col] = consts.FLAG_CELL
    plant_mines()
    teleport.plant_teleports()


def plant_mines():
    global grid
    mines_planted = 0
    while mines_planted < consts.BOARD_ROWS:
        row = random.randint(3, consts.BOARD_ROWS - 1)
        col = random.randint(0, consts.BOARD_COLS - 1)
        if can_place_mine(row, col):
            for cell in range(consts.MINE_COLS):
                grid[row][col + cell] = consts.MINE_CELL
            mines_planted += 1


def can_place_mine(row, col):
    if (row, col) in start_position:
        return False
    for cell in range(consts.MINE_COLS):
        if col + cell >= consts.BOARD_COLS or grid[row][col + cell] != consts.EMPTY_CELL:
            return False
    return True


def hit_mine(legs):
    for leg in legs:
        if grid[leg[0]][leg[1]] == consts.MINE_CELL:
            return True
    return False


def hit_flag(body):
    for cell in body:
        if grid[cell[0]][cell[1]] == consts.FLAG_CELL:
            return True
    return False


def should_draw_mine(row, col):
    if grid[row][col] == consts.MINE_CELL:
        if col == 0 or grid[row][col - 1] != consts.MINE_CELL:
            return True
    return False

def add_soldier_to_grid():
    new_grid = copy.deepcopy(grid)
    sol = soldier.soldier
    if new_grid[sol["row"]][sol["col"]]==consts.EMPTY_CELL:
         new_grid[sol["row"]][sol["col"]]=consts.SOLDIER_CELL
    return new_grid
  
def remove_soldier_from_grid(new_grid):
    row = 0
    col = 0
    for i in range (len(new_grid)):
        for j in range (len(new_grid[i])):
            if new_grid[i][j] == consts.SOLDIER_CELL:
                new_grid[i][j] = consts.EMPTY_CELL
                row = i
                col = j
    global grid
    grid = new_grid
    soldier.load_soldier(row, col)

      
  
