import pandas as pd
import consts
import json


def save(grid, index):
    df = pd.DataFrame(grid)
    db = load_db()
    jdb = df.to_json()
    db[index] = jdb
    save_db(db)



def load(index):
    db = load_db()
    df = json.loads(db[index])
    if df == {}:
        return None
    d = pd.DataFrame(df)
    grid = d.values.tolist()
    return grid


grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]




def start_db():
    grid = []
    df = pd.DataFrame(grid)
    with open("data.json", "a") as f:
        pass
    with open("data.json", "r") as f:
        lines = f.readlines()
    if len(lines) == 0:
        with open("data.json", "a") as f:
            for _ in range(9):
                jdf = df.to_json()
                f.write(jdf + " ")


def load_db():
    with open("data.json", "r") as f:
        lines = f.readlines()
        return lines[0].split(" ")


def save_db(lines):
    with open("data.json", "w") as f:
        for line in lines:
            f.write(line + " ")


