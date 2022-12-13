def set_grid() -> list[list[int]]:
  grid = []

  with open("input.txt", "r") as file:
    for line in file.readlines():
      row = [int(num) for num in line.strip("\n")]
      grid.append(row)

  return grid

def get_best_scenic_score(grid: list[list[int]]) -> int:
  score = 0

  for row_index in range(len(grid)):
    for col_index in range(len(grid[row_index])):
      tree_score = get_scenic_score(grid, (row_index, col_index))
      if tree_score > score:
        score = tree_score

  return score

def get_scenic_score(grid: list[list[int]], coords: (int)) -> int:
  x, y = coords
  tree = grid[x][y]
  # have to reverse top and left lists
  left_side = grid[x][:y][::-1]
  right_side = grid[x][y+1:]
  top_side = [grid[i][y] for i in range(x)][::-1]
  bottom_side = [grid[i][y] for i in range(x+1, len(grid[x]))]
  score = get_score_on_side(tree, left_side) * get_score_on_side(tree, right_side) \
    * get_score_on_side(tree, top_side) * get_score_on_side(tree, bottom_side)
  return score

def get_score_on_side(tree: int, side: list[int]) -> int:
  score = 0

  for num in side:
    score += 1
    if num >= tree:
      break
  
  return score


if __name__ == "__main__":
  grid = set_grid()
  print(get_best_scenic_score(grid))
  