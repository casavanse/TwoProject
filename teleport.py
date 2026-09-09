import consts
import game_field
start_position = [(0, 0), (0, 1),
                  (1, 0), (1, 1),
                  (2, 0), (2, 1),
                  (3, 0), (3, 1)]

grid = game_field.grid()
teleport_list = []
def plant_teleports():
    global grid
    teleports_planted = 0
    while teleports_planted < consts.NUM_OF_TELEPORTS:
        row = random.randint(4, consts.BOARD_ROWS - 4)
        col = random.randint(0, consts.BOARD_COLS - 1)
        if can_place_teleport(row, col):
            for cell in range(consts.TELEPORT_COLS):
                grid[row][col + cell] = consts.TELEPORT_CELL
                teleport_list.append((row,col))
            teleports_planted += 1


def can_place_teleport(row, col):
    if (row, col) in start_position:
        return False
    for cell in range (consts.TELEPORT_COLS):
        if col + cell >= consts.BOARD_COLS or grid[row][col + cell] != consts.EMPTY_CELL:
            return False
    return True


def hit_teleport(legs):
    for leg in legs:
        if grid[leg[0]][leg[1]] == consts.TELEPORT_CELL:
            return True
    return False


def should_draw_teleport(row, col):
    if grid[row][col] == consts.TELEPORT_CELL:
        if col == 0 or grid[row][col - 1] != consts.TELEPORT_CELL:
            return True
    return False

def teleport_launch(current_teleport):
    global teleport_list
    for i in range (len(teleport_list)):
       index = random.randint(0, len(teleport_list) - 1)
       if teleport_list[index] != current_teleport:
          return teleport_list[index]
