import math

with open("day_03/input.txt") as f:
    lists = f.read().splitlines()


def countTrees (right, down, lists):
    row, column, trees = 0, 0, 0
    columns_count = len(lists[0])

    while row < len(lists):
        if lists[row][column] == '#':
            trees += 1
        row += down
        column = (column + right) % columns_count
    print(trees)
    return trees

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

totalTrees = math.prod([countTrees(right, down, lists) for right, down in slopes])

if __name__ == '__main__':
    print(totalTrees)


