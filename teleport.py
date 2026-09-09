import consts
import game_field
start_position = [(0, 0), (0, 1),
                  (1, 0), (1, 1),
                  (2, 0), (2, 1),
                  (3, 0), (3, 1)]

grid = game_field.grid()

def plant_teleports():
    global grid
    mines_planted = 0
    while mines_planted < consts.MINES_COUNT:
        row = random.randint(4, consts.BOARD_ROWS - 4)
        col = random.randint(0, consts.BOARD_COLS - 1)
        if can_place_mine(row, col):
            for cell in range(consts.MINE_COLS):
                grid[row][col + cell] = consts.MINE_CELL
            mines_planted += 1


def can_place_teleport(row, col):
    if (row, col) in start_position:
        return False
    for cell in range (consts.MINE_COLS):
        if col + cell >= consts.BOARD_COLS or grid[row][col + cell] != consts.EMPTY_CELL:
            return False
    return True


def hit_teleport(legs):
    for leg in legs:
        if grid[leg[0]][leg[1]] == consts.TELEPORT_CELL:
            return True
    return False