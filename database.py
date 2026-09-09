import pandas as pd
import consts
import json


def save(grid, index, guard):
    db = load_db()
    df = pd.DataFrame(grid)
    jdb = df.to_json()
    jguard = json.dumps(guard)
    db[index][0] = jdb
    db[index][1] = jguard
    save_db(db)



def load(index):
    db = load_db()
    i = db[index][0]
    df = json.loads(i)
    if not df:
        return None
    d = pd.DataFrame(df)
    grid = d.values.tolist()
    guard = json.loads(db[index][1])
    return grid, guard


grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]




def start_db():
    grid = []
    guard = {}
    jguard = json.dumps(guard)
    df = pd.DataFrame(grid)
    jdf = df.to_json(orient="records")
    with open("data.json", "a") as f:
        pass
    with open("data.json", "r") as f:
        lines = f.readlines()
    if len(lines) == 0:
        with open("data.json", "a") as f:
            for _ in range(9):
                f.write(jdf)
                f.write("@")
                f.write(jguard)
                f.write("\n")


def load_db():
    with open("data.json", "r") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].split("@")
        lines[i][1] = lines[i][1][:-1]
    return lines


def save_db(lines):
    with open("data.json", "w") as f:
        for line in lines:
            line = "@".join(line)
            f.write(line + "\n")

start_db()


g = [[1,1,1],
     [2,2,2],
     [3,3,3]]
guard = {"row": 0, "col": 0, "screen_x": 0, "screen_y": 0}

save(g, 0, guard)
g, guard = load(0)
print(g)
print(guard)