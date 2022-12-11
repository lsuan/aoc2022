from collections import defaultdict

# [Q] [J]                         [H]
# [G] [S] [Q]     [Z]             [P]
# [P] [F] [M]     [F]     [F]     [S]
# [R] [R] [P] [F] [V]     [D]     [L]
# [L] [W] [W] [D] [W] [S] [V]     [G]
# [C] [H] [H] [T] [D] [L] [M] [B] [B]
# [T] [Q] [B] [S] [L] [C] [B] [J] [N]
# [F] [N] [F] [V] [Q] [Z] [Z] [T] [Q]
#  1   2   3   4   5   6   7   8   9 

def open_file() -> list[str]:
  with open("input.txt", "r") as file:
    return file.readlines()

# returns [(amount_number, from_crate, to_crate)]
def get_commands(file_lines: list[str]) -> list[tuple[int]]:
  commands = []
  for line in file_lines:
    line = line.strip("\n")
    if "move" in line:
      command_line = line.split()
      commands.append((int(command_line[1]), int(command_line[3])-1, int(command_line[5])-1))
  return commands

def rearrange_crates(stacks: defaultdict[int, list], commands: list[tuple[int]], rearrange: callable) -> defaultdict[int, list]:
  rearranged = stacks.copy()
  
  for command in commands:
    amount = command[0]
    # need to make a copy here so that it points to a different memory block
    from_stack = rearranged[command[1]].copy()
    to_stack = rearranged[command[2]].copy()
    rearrange(amount, from_stack, to_stack)
    rearranged[command[1]] = from_stack
    rearranged[command[2]] = to_stack

  return rearranged

def rearrange_by_reverse_order(amount: int, from_stack: list[str], to_stack: list[str]):
  for _ in range(amount):
    crate = from_stack.pop()
    to_stack.append(crate)

def rearrange_crates_in_order(amount: int, from_stack: list[str], to_stack: list[str]):
  removed = []
  for _ in range(amount):
    removed.append(from_stack.pop())
  to_stack.extend(reversed(removed))

def get_stacks(file_lines: list[str]) -> list[list]:
  stacks = defaultdict(list)
  for line in file_lines:
    if "1" in line:
      break

    stack_index = 0
    for i in range(0, len(line), 4):
      crate = line[i:i+3]
      if not crate.isspace():
        stacks[stack_index].append(crate[1])
      stack_index += 1

  # reversing the stacks so the top crate appears at the end of the lsit
  for stack_index, stack in stacks.items():
    stacks[stack_index] = list(reversed(stack))
  
  return stacks

def get_top_crates(stacks: defaultdict[int, list]) -> str:
  result = ""
  for stack_index in sorted(stacks.keys()):
    result += stacks[stack_index][-1]
  return result

if __name__ == "__main__":
  file_lines = open_file()
  stacks = get_stacks(file_lines)
  commands = get_commands(file_lines)
  rearranged = rearrange_crates(stacks, commands, rearrange_by_reverse_order)

  # Part 1 Solution
  print(get_top_crates(rearranged))
  
  # Part 2 Solution
  rearranged = rearrange_crates(stacks, commands, rearrange_crates_in_order)
  print(get_top_crates(rearranged))