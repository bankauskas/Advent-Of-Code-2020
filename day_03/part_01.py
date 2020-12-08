with open("day_03/input.txt") as f:
    lists = f.read().splitlines()

columns_count = len(lists[0])
right, down = 3, 1
row, column, trees = 0, 0, 0

while row < len(lists):
    if lists[row][column] == '#':
        trees += 1
    row += down
    column = (column + right) % columns_count

if __name__ == '__main__':
    print(trees)

    