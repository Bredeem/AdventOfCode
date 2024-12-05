
INPUT_FILE = "input.txt"

def find_relevant_rules(rules: list[tuple[int]], update: list[int]):
    relevant_rules = []
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            relevant_rules.append(rule)
    return relevant_rules
             
def check_update(rules: list[tuple[int]], update: list[int]):
    
    for n in update:
        for rule in rules:
            if n == rule[0]:
                if update.index(n) > update.index(rule[1]):
                    return False
            elif n == rule[1]:
                if update.index(n) < update.index(rule[1]):
                    return False

    return True

def correct_update(rules: list[tuple[int]], update: list[int]):

    while not check_update(rules, update):
        for n in update:
            for rule in rules:
                if n == rule[0]:
                    if update.index(n) > update.index(rule[1]):
                        update.insert(update.index(rule[1]), update.pop(update.index(n)))
                elif n == rule[1]:
                    if update.index(n) < update.index(rule[1]):
                        update.insert(update.index(rule[1]+1), update.pop(update.index(n)))
    
    return update  


def part1(rules: list[tuple[int]], updates: list[list[int]]):
    
    sum = 0

    for update in updates:
        relevant_rules = find_relevant_rules(rules, update)
        if check_update(relevant_rules, update):
            sum += update[len(update)//2]
            
    print(f"Part 1: {sum}")

def part2(rules: list[tuple[int]], updates: list[list[int]]):
    
    sum = 0

    for update in updates:
        relevant_rules = find_relevant_rules(rules, update)
        if not check_update(relevant_rules, update):
        
            update = correct_update(relevant_rules, update)
            if not check_update(relevant_rules, update):
                print("Upsie")
            sum += update[len(update)//2]

            
    print(f"Part 2: {sum}")




def main():
    
    with open(INPUT_FILE, "r") as f:
        input_string = f.read()
    
    part_a, part_b = input_string.split("\n\n")
    rules = [(int(rule.split("|")[0]), int(rule.split("|")[1])) for rule in part_a.split()]

    updates = []
    for update in part_b.split():
        updates.append([int(n) for n in update.split(",")])

    # print(updates)

    part1(rules, updates)
    part2(rules, updates)

if __name__ == '__main__':
    main()