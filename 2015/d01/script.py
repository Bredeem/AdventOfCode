
INPUT_FILE = "input.txt"

def part1(string: str):
    floor = string.count("(") - string.count(")")
    print(f"Part 1: {floor}")

def part2(string: str):
    pos = 1
    floor = 0
    for c in string:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        
        if floor < 0:
            break
        pos += 1
    
    print(f"Part 2: {pos}")



def main():
    
    with open(INPUT_FILE, "r") as f:
        input_string = f.read()

    part1(input_string)
    part2(input_string)

if __name__ == '__main__':
    main()