class Dir:
  def __init__(self, name: str):
    self.content = {} # keys -> names, values -> type (dir or file)
    self.name = name

  def set_content(self, name: str, content = None):
    self.content[name] = content

  def get_content(self):
    return self.content

  def get_name(self):
    return self.name

  def get_size(self):
    size = 0
    for name, content in self.content:
      size += content.get_size()
    return size

class File:
  def __init__(self, name: str, size: int):
    self.name = name
    self.size = size

  def get_content(self):
    return self.name

  def get_size(self):
    return self.size

def set_file_system() -> dict[str, Dir | File]:
  file_system: dict[str, Dir | File] = {}
  current: str = ""

  with open("input.txt", "r") as file:
    for line in file.readlines():
      line = line.strip("\n").split()
      if line[0] == "$":
        command = line[1]
        match command:
          case "cd":
            if line[2] == "..":
              current = find_parent_dir(file_system, current)
              # go back in the tree and find the parent
            else:
              current = line[2]
              if current not in file_system:
                file_system[current] = Dir(current)
          # Don't need to account for ls since current one is set on cd
      elif line[0] == "dir":
        file_system[current].set_content(Dir(line[1]))
      elif line[0].isdigit():
        file_system[current].set_content(File(line[1], line[0]))
  return file_system

def find_parent_dir(file_system: dict[str, Dir | File], name: str, parent: str = "/", visited: list = []) -> str:
  if parent not in visited and name in file_system[parent].get_content():
    return parent
  else:
    visited.append(parent)
    for child in file_system[name].get_content():
      print(child.get_name())
      if type(child) == Dir:
        find_parent_dir(file_system, name, child.get_name(), visited)
    
if __name__ == "__main__":
  files = set_file_system()
  # print(files["/"].get_content())