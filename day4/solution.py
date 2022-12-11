def open_file() -> list[str]:
  with open("input.txt", "r") as file:
    return file.readlines()

def get_overlapping_pairs(file_lines: list[str], in_range: callable):
  pairs = 0

  for line in file_lines:
    pair = line.strip("\n").split(",")
    first_assignments = get_assignment_range(pair[0])
    second_assigments = get_assignment_range(pair[1])
    if in_range(first_assignments, second_assigments):
      pairs += 1

  return pairs
      
def is_fully_in_range(first: list[int], second: list[int]) -> bool:
  first_range = range(first[0], first[1]+1)
  second_range = range(second[0], second[1]+1)
  return (first[0] in second_range and first[1] in second_range) \
    or (second[0] in first_range and second[1] in first_range)

def is_in_range(first: list[int], second: list[int]) -> bool:
  first_range = range(first[0], first[1]+1)
  second_range = range(second[0], second[1]+1)
  return (first[0] in second_range or first[1] in second_range) \
    or (second[0] in first_range or second[1] in first_range)

def get_assignment_range(string_range: str) -> list[int]:
  list_range = string_range.split("-")
  return [int(i) for i in list_range]

if __name__ == "__main__":
  inputs = open_file()

  # Part 1 solution
  print(get_overlapping_pairs(inputs, is_fully_in_range))

  # Part 2 solution
  print(get_overlapping_pairs(inputs, is_in_range))
