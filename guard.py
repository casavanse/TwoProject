import consts
import soldier

guard = {}

def create():
    global guard
    guard = {"row" : consts.GUARD_ROWS, "col" : consts.GUARD_START_COLS,
             "screen_x" : consts.GUARD_START_COLS * consts.CELL_SIZE, "screen_y" : consts.GUARD_ROWS * consts.CELL_SIZE,
             "direction" : True} #True: right, False: left

def move():
    global guard
    if guard["col"] == consts.BOARD_COLS - 1 or guard["col"] == 0:
        guard["direction"] = not guard["direction"]
    if guard["direction"]:
        guard["col"] += 1
    else:
        guard["col"] -= 1

    guard["screen_x"] = guard["col"] * consts.CELL_SIZE

def get_guard_body():
    body = []
    for row in range(consts.SOLDIER_ROWS):
        for col in range(consts.SOLDIER_COLS):
            body.append((guard["row"] + row, guard["col"] + col))
    return body

def hit_guard():
    sol_body = soldier.get_soldier_body()
    guard_body = get_guard_body()
    for part in sol_body:
        if part in guard_body:
            return True
    return False



