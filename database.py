import pandas as pd
import consts

def save(grid, index):
    df = pd.DataFrame(grid)
    df.to_json("data.json", orient="split", compression="infer")

def load(index):
    df = pd.read_json("data.json", orient="split", compression="infer")
    grid = df.values.tolist()
    return grid

grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
# save(grid)
# print("=======")
# grid = load()
# print(grid)


def start_db():
    grid = []
    df = pd.DataFrame(grid)
    with open("data.json", "w") as f:
        for _ in range(9):
            df.to_csv(f, index=False, mode='a', lineterminator='\n')

# start_db()
save(grid, 0)
grid = load()
print(grid)
