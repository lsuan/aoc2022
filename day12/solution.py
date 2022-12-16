def get_map() -> tuple[list[list[str]], list[tuple[int,int]]]:
  heightmap = []
  coords = [(0, 0), (0, 0)] # (row, col)
  with open("input.txt", "r") as file:
    lines = file.readlines()
    for line_index in range(len(lines)):
      section = []
      line = lines[line_index]
      line = line.strip("\n")
      for i in range(len(line)):
        char = line[i]
        if char == "S":
          coords[0] = (line_index, i)
        elif char == "E":
          coords[1] = (line_index, i)
        section.append(char)
      heightmap.append(section)
  return heightmap, coords[0], coords[1]

def traverse(heightmap: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> int:
  visited = []
  path = []
  current = start
  while current != end:
    print(heightmap[current[0]][current[1]], current)
    if current not in visited:
      visited.append(current)
      path.append(current)
    
    neighboring_moves = get_neighbors(heightmap, current[0], current[1], visited)
    if neighboring_moves == []:
      prev_step = len(path) - 1
      path = path[:prev_step]
      current = path[-1]
    else:
      current = neighboring_moves[0]
    
  return len(path)

def get_neighbors(heightmap: list[list[str]], row_index: int, col_index: int, visited: list[tuple[int, int]]) -> tuple[int, int]:
  available_moves = []
  if row_index == 0 and col_index == 0:
    # top left corner
    top = None
    left = None
    right = row_index, col_index + 1
    bottom = row_index + 1, col_index
  elif row_index == len(heightmap) - 1 and col_index == 0:
    # bottom left corner
    bottom = None
    left = None
    top = row_index - 1, col_index
    right = row_index, col_index + 1
  elif row_index == 0 and col_index == len(heightmap[0]) -1:
    # top right corner
    top = None
    right = None
    bottom = row_index + 1, col_index
    left = row_index, col_index - 1
  elif row_index == len(heightmap) - 1 and col_index == len(heightmap[0]) -1:
    # bottom right corner
    bottom = None
    right = None
    top = row_index - 1, col_index
    left = row_index, col_index - 1
  elif row_index == 0:
    # top row only
    top = None
    right = row_index, col_index + 1
    bottom = row_index + 1, col_index
    left = row_index, col_index - 1
  elif row_index == len(heightmap) - 1:
    # bottom row only
    bottom = None
    top = row_index - 1, col_index
    right = row_index, col_index + 1
    left = row_index, col_index - 1
  elif col_index == 0:
    # left col only
    left = None
    top = row_index - 1, col_index
    right = row_index, col_index + 1
    bottom = row_index + 1, col_index
  elif col_index == len(heightmap[0]) -1:
    # right col only
    right = None
    top = row_index - 1, col_index
    bottom = row_index + 1, col_index
    left = row_index, col_index - 1
  else:
    top = row_index - 1, col_index
    bottom = row_index + 1, col_index
    left = row_index, col_index - 1
    right = row_index, col_index + 1
  available_moves.extend([top, bottom, left, right])
  
  valid_moves = sorted([move for move in available_moves if is_valid_move(move, visited)], key=lambda x: heightmap[x[0]][x[1]], reverse=True)
  if heightmap[row_index][col_index] == "S":
    return valid_moves
  
  if heightmap[row_index][col_index] == "z":
    for move in valid_moves:
      if heightmap[move[0]][move[1]] == "E":
        return [move]
  
  return [move for move in valid_moves if is_equal_or_ascending(heightmap, move, row_index, col_index)]

def is_equal_or_ascending(heightmap: list[list[str]], move: tuple[int, int], row_index: int, col_index: int) -> bool:
  return ord(heightmap[move[0]][move[1]]) - ord(heightmap[row_index][col_index]) in [0, 1]

def is_valid_move(move: tuple[int, int], visited: list[tuple[int, int]]) -> bool:
  return move is not None and move not in visited

if __name__ == "__main__":
  heightmap, start, end = get_map()
  print(traverse(heightmap, start, end))
