from collections import defaultdict

def set_directories() -> list[dict]:
  files = {}
  history = [] # history of traversed directories
  current_dir_name = ""

  with open("input.txt", "r") as file:
    for line in file.readlines():
      line = line.strip("\n").split()
      if line[0] == "$":
        match line[1]:
          case "cd":
            if line[2] == "..":
              history.pop()
            else:
              history.append(line[2])
              files["_".join(history)] = None
            # '_' indicates subdirectory; not using '/' since root directory is already '/'
            current_dir_name = "_".join(history)
      elif line[0] == "dir":
        files[current_dir_name] = None
      elif line[0].isdigit():
        files[current_dir_name+"_"+line[1]] = int(line[0])
  
  return files

def get_total_sizes(files_system: dict) -> defaultdict[str, int]:
  sizes = defaultdict(int)
  total_sizes = defaultdict(int)

  for name, value in files_system.items():
    if isinstance(value, int):
      dir_name = "_".join(name.split("_")[:-1])
      sizes[dir_name] += value
  
  for name, value in sizes.items():
    dirs = name.split("_")
    for i in range(len(dirs)):
      total_sizes["_".join(dirs[0:i+1])] += value
      
  return total_sizes

def get_size_of_dir_to_delete(sizes: dict) -> int:
  total = sizes["/"]
  update_size = 30000000
  available = 70000000
  space_left = available - total
  space_to_delete = update_size - space_left
  biggest_sizes = filter(lambda item: item[1] >= space_to_delete, sizes.items())
  return sorted(biggest_sizes, key=lambda item: item[1])[0][1]
  

if __name__ == "__main__":
  files = set_directories()
  sizes = get_total_sizes(files)
  total_of_small_sizes = sum(filter(lambda item: item <= 100000, sizes.values()))

  # Part 1 solution
  print(total_of_small_sizes)
  
  # Part 2 solution
  print(get_size_of_dir_to_delete(sizes))
