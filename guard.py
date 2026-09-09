import consts


guard = {}

def create():
    global guard
    guard = {"row" : 0, "col" : 0,
             "screen_x" : consts.GUARD_START_COLS, "screen_y" : consts.GUARD_ROWS}