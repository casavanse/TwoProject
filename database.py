import pandas as pd

def save(grid):
    with open("data.csv", "a") as file:
        df = pd.DataFrame(grid)
        print(df)
        df.to_csv(file)

grid = [[1,2,3],
        [4,5,6],
        [7,8,9]]
save(grid)