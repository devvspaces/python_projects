"""
Code to create a grid of i x j
"""


def print_grid(grid):
    """
    Takes any grid and prints it out in a nice format
    """
    print('-' * len(grid[0]) * 5)
    for x in grid:
        for y in x:
            print(f"| {y} ", end="")

        print('|')
        print('-' * len(x) * 5)


def create_grid(i, j):
    """
    Takes i(row) and j(col) and returns a grid of size i x j
    """
    grid = []
    for x in range(i):
        row = []
        for y in range(j):
            row.append(f"{x}{y}")

        grid.append(row)
        row = []

    return grid


grid = create_grid(5, 5)
print_grid(grid)


def traverse(start_cell, direction, num_steps):
    stride = []
    for step in range(num_steps):
        row = start_cell[0] + step * direction[0]
        col = start_cell[1] + step * direction[1]
        stride.append((row, col,))
    return stride


# up = traverse(
#     (0, 0),
#     (0, 1),
#     5
# )

# for top in up:
#     print(traverse(
#         top,
#         (1,0),
#         5
#     ))

diagonal_x = traverse(
    (0, 0),
    (1, 1),
    5
)
print(diagonal_x)
