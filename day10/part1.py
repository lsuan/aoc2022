def get_signal_strengths() -> int:
  signal_strengths = []
  cycles_to_check = [20, 60, 100, 140, 180, 220]
  current_cycle = 0
  x = 1

  with open("input.txt", "r") as file:
    for line in file.readlines():
      line = line.strip("\n").split()

      if line[0] == "addx":
        for _ in range(2):
          current_cycle = execute_cycle(current_cycle, cycles_to_check, signal_strengths, x)
        x += int(line[1])
      else:
        current_cycle = execute_cycle(current_cycle, cycles_to_check, signal_strengths, x)
        if current_cycle in cycles_to_check:
          signal_strengths.append(current_cycle * x)

  return sum(signal_strengths)

def execute_cycle(current_cycle: int, cycles_to_check: list[int], signal_strengths: list[int], x: int) -> int:
  current_cycle += 1            
  if current_cycle in cycles_to_check:
    signal_strengths.append(current_cycle * x)
  return current_cycle

if __name__ == "__main__":
  print(get_signal_strengths())