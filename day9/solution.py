

def get_num_visited() -> int:
  head_visited = [(0, 0)]
  tail_visited = [(0, 0)]

  with open("input.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
      line = line.strip("\n")
      direction, count = line[0], int(line[2])
      head_x, head_y = head_visited[-1]
      tail_x, tail_y = tail_visited[-1]
      print(direction, count)
      # R -> +x, L -> -x, U -> +y, D -> -y
      match direction:
        case "R":
          for _ in range(count):
            head_x += 1

            if head_y == tail_y and abs(head_x - tail_x) > 1:
              tail_x += 1
              tail_visited.append((tail_x, tail_y))
            elif head_y < tail_y and abs(head_x - tail_x) > 1:
              tail_y -= 1
              tail_x += 1
              tail_visited.append((tail_x, tail_y))
            elif head_y > tail_y and abs(head_x - tail_x) > 1:
              tail_y += 1
              tail_x += 1
              tail_visited.append((tail_x, tail_y))

            head_visited.append((head_x, head_y))
            

        case "L":
          for _ in range(count):
            head_x -= 1

            # was tail-x - head_x
            if head_y == tail_y and abs(head_x - tail_x) > 1:
              tail_x -= 1
              tail_visited.append((tail_x, tail_y))
            elif head_y < tail_y and abs(head_x - tail_x) > 1:
              tail_y -= 1
              tail_x -= 1
              tail_visited.append((tail_x, tail_y))
            elif head_y > tail_y and abs(head_x - tail_x) > 1:
              tail_y += 1
              tail_x -= 1
              tail_visited.append((tail_x, tail_y))

            head_visited.append((head_x, head_y))
            

        case "U":
          for _ in range(count):
            head_y += 1

            if head_x == tail_x and abs(head_y - tail_y) > 1:
              tail_y += 1
              tail_visited.append((tail_x, tail_y))
            elif head_x < tail_x and abs(head_y - tail_y) > 1:
              tail_x -= 1
              tail_y += 1
              tail_visited.append((tail_x, tail_y))
            elif head_x > tail_x and abs(head_y - tail_y) > 1:
              tail_x += 1
              tail_y += 1
              tail_visited.append((tail_x, tail_y))

            head_visited.append((head_x, head_y))
            

        case "D":
          for _ in range(count):
            head_y -= 1

            # was tail_y - head_y
            if head_x == tail_x and abs(head_y - tail_y) > 1:
              tail_y -= 1
              tail_visited.append((tail_x, tail_y))
            elif head_x < tail_x and abs(head_y - tail_y) > 1:
              tail_x -= 1
              tail_y -= 1
              tail_visited.append((tail_x, tail_y))
            elif head_x > tail_x and abs(head_y - tail_y) > 1:
              tail_x += 1
              tail_y -= 1
              tail_visited.append((tail_x, tail_y))

            head_visited.append((head_x, head_y))
            
  return len(set(tail_visited))

if __name__ == "__main__":
  print(get_num_visited())