import pandas as pd


def save(grid):
    df = pd.DataFrame(grid)
    print(df)
    df.to_csv("data.csv", lineterminator='\n', header=False)

def load():
    with open("data.csv", "r") as file:
        df = pd.read_csv(file)
        print(df)
        l = df.values.tolist()
        print(l)

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
save(grid)
load()
