from string import ascii_letters

priorities = {}
for i in range(len(ascii_letters)):
  priorities[ascii_letters[i]] = i+1

def get_priorities():
  item_priorities = []

  with open("input.txt", "r") as file:
    for line in file.readlines():
      line = line.strip("\n")
      mid = len(line) // 2
      first_compartment = line[:mid]
      second_compartment = line[mid:]
      same_letter = find_same_letter(first_compartment, second_compartment)
      item_priorities.append(priorities[same_letter])
      
  return item_priorities

# gets the intersection of the sets -> same letter
def find_same_letter(first, second) -> str:
  first_set = set(first)
  second_set = set(second)
  intersection = first_set & second_set
  return next(intersection.__iter__())

if __name__ == "__main__":
  item_priorities = get_priorities()
  print(sum(item_priorities))