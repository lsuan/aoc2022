points_distribution = {
  "A": 1, "B": 2, "C": 3,
}

def get_total_points():
  points: int = 0

  with open("input.txt", "r") as file:
    for line in file.readlines():
      line = line.split()
      enemy_move, expected_result = line[0], line[1]
      points += get_points_from_round(enemy_move, expected_result)

  return points

# X -> lose, Y -> draw, Z -> win
# A -> rock, B -> paper, C -> scissors
# rock = 1, paper = 2, scissors = 3
def get_points_from_round(enemy_move: str, expected_result: str) -> int:
  if expected_result == "Y":
    return points_distribution[enemy_move] + 3
  elif expected_result == "X":
    if enemy_move == "A":
      return 3
    elif enemy_move == "B":
      return 1
    else:
      return 2
  elif expected_result == "Z":
    if enemy_move == "A":
      return 2 + 6
    elif enemy_move == "B":
      return 3 + 6
    else:
      return 1 + 6

if __name__ == "__main__":
  points = get_total_points()
  print(points)