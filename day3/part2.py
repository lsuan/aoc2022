from string import ascii_letters

priorities = {}
for i in range(len(ascii_letters)):
  priorities[ascii_letters[i]] = i+1

def get_group_priorities():
  group_priorities = []

  with open("input.txt", "r") as file:
    groups = get_elf_groups(file.readlines())
    for group in groups:
      sets = [set(subgroup) for subgroup in group.split()]
      same_letter = get_same_letter(sets[0], sets[1], sets[2])
      group_priorities.append(priorities[same_letter])

  return group_priorities

def get_elf_groups(lines: list[str]) -> list[str]:
  groups = []

  for i in range(0, len(lines), 3):
    group = lines[i] + lines[i+1] + lines[i+2].strip("\n")
    groups.append(group)

  return groups

def get_same_letter(set1: set, set2: set, set3: set) -> str:
  same_letter = set1 & set2 & set3
  return next(same_letter.__iter__())


if __name__ == "__main__":
  group_priorities = get_group_priorities()
  print(sum(group_priorities))