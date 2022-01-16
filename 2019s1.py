# 2019 Senior 1


def flip_h(grid):
    temp = grid[0][0]
    grid[0][0] = grid[1][0]
    grid[1][0] = temp

    temp = grid[0][1]
    grid[0][1] = grid[1][1]
    grid[1][1] = temp

    return grid


def flip_v(grid):
    temp = grid[0][0]
    grid[0][0] = grid[0][1]
    grid[0][1] = temp

    temp = grid[1][0]
    grid[1][0] = grid[1][1]
    grid[1][1] = temp

    return grid


grid_test = [[1, 2], [3, 4]]

command = input().strip(" .,!")

horizontal_flip = True if command.count('H') % 2 == 1 else False
vertical_flip = True if command.count('V') % 2 == 1 else False

if horizontal_flip:
    flip_h(grid_test)
if vertical_flip:
    flip_v(grid_test)

print(f"{grid_test[0][0]} {grid_test[0][1]}")
print(f"{grid_test[1][0]} {grid_test[1][1]}")
