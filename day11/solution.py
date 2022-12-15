from collections import defaultdict

def get_monkeys() -> list[dict]:
  monkeys = []

  with open("sample.txt", "r") as file:
    for block in file.read().split("\n\n"):
      block = block.strip().split("\n")
      monkey = {}
      for i in range(len(block)-2):
        line = block[i].split()
        if i == 0:
          monkey["id"] = int(line[-1][0])
        elif i == 1:
          monkey["items"] = sanitize_items(line[2:])
        elif i == 2:
          monkey["operation"] = eval(sanitize_operation(line[-2:]))
        elif i == 3:
          monkey["mod_condition"] = int(line[-1])
          monkey["true_pass"] = int(block[i+1][-1])
          monkey["false_pass"] = int(block[i+2][-1])
      monkeys.append(monkey)
  return monkeys

def get_monkey_business(monkeys: list) -> int:
  inspections = defaultdict(int)

  for _ in range(1000):
    print(_)
    for monkey in monkeys:
      while monkey["items"] != []:
        item = monkey["items"].pop(0)
        inspections[monkey["id"]] += 1
        func = monkey["operation"]
        new_worry = func(item)
        # Part 1 worry
        # new_worry = new_worry // 3
        # Part 2 worry
        new_worry = new_worry // len(monkeys) * (len(monkey["items"]) + 1)
        if new_worry % monkey["mod_condition"] == 0:
          monkeys[monkey["true_pass"]]["items"].append(new_worry)
        else:
          monkeys[monkey["false_pass"]]["items"].append(new_worry)

  most_active = sorted(inspections.values(), reverse=True)[:2]
  return most_active[0] * most_active[1]

def sanitize_items(items: list[str]) -> list[int]:
  sanitized = []
  for item in items:
    if item[-1] == ",":
      item = item[:-1]
    sanitized.append(int(item))
  return sanitized

def sanitize_operation(operation: list[str]) -> str:
  return f"lambda x: x {operation[0]} {'x' if operation[1] == 'old' else operation[1]}"

if __name__ == "__main__":
  monkeys = get_monkeys()
  print(get_monkey_business(monkeys))