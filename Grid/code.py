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


if __name__ == '__main___':
    grid = create_grid(1,9)
    print_grid(grid)