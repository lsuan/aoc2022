import math

def compare_pairs() -> int:
  correct_indices = set()

  with open("sample.txt", "r") as file:
    pairs = file.read().split("\n\n")
    for i in range(len(pairs)):
      lists = []
      for line in pairs[i].split():
        lists.append(eval(line))
      
      if len(lists[0]) > len(lists[1]):
        continue
      elif len(lists[0]) < len(lists[1]):
        correct_indices.add(i+1)
      
      if is_correct(lists):
        correct_indices.add(i + 1)

  print(correct_indices)
  return sum(list(correct_indices))

def is_correct(pairs: list[list]) -> bool:
  for i in range(len(pairs[0])):
    value1 = pairs[0][i]
    value2 = pairs[1][i]

    print(value1, "vs", value2)
    if type(value1) is int and type(value2) is int:
      if value1 == value2:
        continue
      else:
        return value1 < value2
    elif type(value1) is int and type(value2) is list:
      value2 = flatten(value2)
      if value1 == value2[0]:
        continue
      else:
        return value1 < value2[0]
    elif type(value1) is list and type(value2) is int:
      value1 = flatten(value1)
      if value1[0] == value2:
        continue
      else:
        return value1[0] < value2
    else:
      value1 = flatten(value1)
      value2 = flatten(value2)
      if value1 == [] and value2 != []:
        return True
      if value2 == []:
        return False

      while value1 != []:
        if value1[0] == value2[0]:
          value1.pop(0)
          value2.pop(0)
          continue
        return value1[0] < value2[0]
  
  return is_correct

def flatten(l):
  flatlist = []
  for element in l:
    if type(element) is list:
      flatlist += flatten(element)
    else:
      flatlist += [element]
  return flatlist
# def is_correct(pairs: list[list]) -> bool:
#   is_correct = True
#   for i in range(len(pairs[0])):
#     value1 = pairs[0][i]
#     value2 = pairs[1][i]
#     print(value1, "vs", value2)
#     is_correct = is_correct_value(value1, value2)
#     print(is_correct, "\n")
#     if is_correct:
#       return True
    
#   return is_correct

# def is_correct_value(value1, value2) -> bool:
#   print(value1, "in icv", value2)
#   if type(value1) is int and type(value2) is int:
#     return value1 < value2
#   elif type(value1) is list and type(value2) is list:
#     if value1 == [] and value2 != []:
#       return True
#     if value2 == []:
#       return False
#     for vi in range(len(value1)):
#       if vi == len(value2):
#         return False
#       if is_correct_value(value1[vi], value2[vi]):
#         return True
#     return False
#   elif type(value1) is int and type(value2) is list:
#     return is_correct_value([value1], value2)
#   elif type(value1) is list and type(value2) is int:
#     return is_correct_value(value1, [value2])

if __name__ == "__main__":
  print(compare_pairs())
  # 6071 too high