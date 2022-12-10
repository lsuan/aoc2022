def get_calories_per_elf() -> list[int]:
  calories: list[int] = [0]

  with open("input.txt", 'r') as file:
    i = 0
    for line in file.readlines():
      line = line.strip("\n")
      if line == "":
        i += 1
        calories.append(0)
      else:
        calories[i] += int(line)
  
  return calories

if __name__ == "__main__":
  calories = get_calories_per_elf()
  max_calories = max(calories)

  # part 1 solution
  print(max_calories)
  
  # part 2 solution
  sorted_calories = sorted(calories, reverse=True)
  top3 = sorted_calories[:3]
  print(sum(top3))