points_distribution = {
  "A": 1, "B": 2, "C": 3,
  "X": 1, "Y": 2, "Z": 3
}

def get_total_points() -> int:
  points: int = 0

  with open("input.txt", "r") as file:
    for line in file.readlines():
      line = line.split()
      enemy_move, my_move = line[0], line[1]
      round_result = get_round_result(enemy_move, my_move)
      match round_result:
        case "win":
          points += points_distribution[my_move] + 6
        case "draw":
          points += points_distribution[my_move] + 3
        case "lose":
          points += points_distribution[my_move]

  return points

# A, X = rock
# B, Y = paper
# C, Z = scissors
def get_round_result(enemy_move: str, my_move: str) -> str:
  if points_distribution[enemy_move] == points_distribution[my_move]:
    return "draw"
  elif enemy_move == "A" and my_move == "Y":
    return "win"
  elif enemy_move == "A" and my_move == "Z":
    return "lose"
  elif enemy_move == "B" and my_move == "X":
    return "lose"
  elif enemy_move == "B" and my_move == "Z":
    return "win"
  elif enemy_move == "C" and my_move == "X":
    return "win"
  elif enemy_move == "C" and my_move == "Y":
    return "lose"

if __name__ == "__main__":
  points = get_total_points()
  print(points)