def produce_crt_drawing() -> str:
  crt = []
  crt_row = ""
  cycles_to_check = [40, 80, 120, 160, 200, 240]
  draw_position = 0
  sprite_position = [0, 1, 2]
  x = 1

  with open("input.txt", "r") as file:
    for line in file.readlines():
      line = line.strip("\n").split()

      if line[0] == "addx":
        for _ in range(2):
          crt_row, draw_position = execute_cycle(crt_row, crt, draw_position, sprite_position, cycles_to_check)
        x += int(line[1])
        for i in range(len(sprite_position)):
          sprite_position[i] = x + i
      
      else:
        crt_row, draw_position = execute_cycle(crt_row, crt, draw_position, sprite_position, cycles_to_check)
        

  return "\n".join(crt)

def execute_cycle(crt_row: list[str], crt: str, draw_position: int, sprite_position: int, cycles_to_check: list[int]) -> tuple[str, int]:
  draw_position += 1

  if draw_position in sprite_position:
    crt_row += "#"
  else:
    crt_row += "."
  if draw_position in cycles_to_check:
    crt.append(crt_row)
    crt_row = ""
    draw_position = 0
  return (crt_row, draw_position)

if __name__ == "__main__":
  print(produce_crt_drawing())