def set_grid() -> list[list[int]]:
  grid = []

  with open("input.txt", "r") as file:
    for line in file.readlines():
      row = [int(num) for num in line.strip("\n")]
      grid.append(row)

  return grid

def find_all_visible_trees(grid: list[list[int]]) -> int:
  count = 0

  for row_index in range(len(grid)):
    for col_index in range(len(grid[row_index])):
      if is_visible(grid, (row_index, col_index)):
        count += 1

  return count

def is_visible(grid: list[list[int]], coords: (int)) -> bool:
  x, y = coords
  # if tree is on the edge
  # -> tree is on the first row / last row / first col / last col
  if (x == 0) or (x == len(grid) - 1) or (y == 0) or (y == len(grid[x]) - 1):
    return True

  tree = grid[x][y]
  left_side = grid[x][:y]
  right_side = grid[x][y+1:]
  top_side = [grid[i][y] for i in range(x)]
  bottom_side = [grid[i][y] for i in range(x+1, len(grid[x]))]

  return is_visible_on_side(tree, left_side) or is_visible_on_side(tree, right_side) \
    or is_visible_on_side(tree, top_side) or is_visible_on_side(tree, bottom_side)

def is_visible_on_side(tree: int, side: list[int]) -> bool:
  return all([n < tree for n in side])

if __name__ == "__main__":
  grid = set_grid()
  print(find_all_visible_trees(grid))