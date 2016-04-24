def count_neighbours(grid, row, col):
    count = 0

    rows = len(grid)
    cols = len(grid[0])

    for i in range(row - 1, row + 2):
        if 0 <= i < rows:
            for j in range(col - 1, col + 2):
                if 0 <= j < cols:
                    if grid[i][j] > 0:
                        count += 1
    count -= grid[row][col]

    return count


if __name__ == '__main__':
    ''' # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example" '''
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
