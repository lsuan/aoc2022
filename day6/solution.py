def find_first_marker_count(string: str, marker_length: int) -> int:
  for i in range(len(string)):
    substr = string[i:i+marker_length]
    if len(set(substr)) == marker_length:
      return i+marker_length

if __name__ == "__main__":
  with open("input.txt", "r") as file:
    datastream = file.readline()

  # Part 1 solution
  # print(find_first_marker_count(datastream, 4))

  # Part 2 solution
  print(find_first_marker_count(datastream, 14))
