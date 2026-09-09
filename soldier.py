import consts

soldier = {}

def create_soldier():
    global soldier
    soldier = {"row": 0, "col": 0, "screen_x":0,"screen_y":0}

def can_move(direction):
    if direction == consts.UP:
        if soldier["row"] == 0:
            return False
    if direction == consts.DOWN:
        if soldier["row"]+3 >= consts.BOARD_ROWS-1:
            return False
    if direction == consts.LEFT:
        if soldier["col"] == 0:
            return False
    if direction == consts.RIGHT:
        if soldier["col"] + 1 >= consts.BOARD_COLS-1:
            return False
    return True



def move(direction):
    if not can_move(direction):
        return
    global soldier
    soldier["row"] += direction[0]
    soldier["col"] += direction[1]
    soldier["screen_y"] = soldier["row"]*consts.CELL_SIZE
    soldier["screen_x"] = soldier["col"]*consts.CELL_SIZE


def get_soldier_body():
    global soldier
    soldier_body = [(soldier["row"], soldier["col"]),
                    (soldier["row"], soldier["col"]+1),
                    (soldier["row"]+1, soldier["col"]),
                    (soldier["row"]+1, soldier["col"]+1),
                    (soldier["row"]+2, soldier["col"]+1),
                    (soldier["row"]+2, soldier["col"])]
    return soldier_body


def get_soldier_feet():
    global soldier
    soldier_feet = [(soldier["row"]+3, soldier["col"]),
                    (soldier["row"]+3, soldier["col"]+1)]
    return soldier_feet



def load_soldier(row,col):
    global soldier
    soldier["row"] = row
    soldier["col"] = col
    soldier["screen_y"] = soldier["row"]*consts.CELL_SIZE
    soldier["screen_x"] = soldier["col"]*consts.CELL_SIZE
    
