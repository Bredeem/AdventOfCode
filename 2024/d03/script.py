import re

def find_and_multiply_with_cond(string: str):
    li = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", string)

    res = 0

    enabled = True

    for s in li:
        if s == "don't()":
            enabled = False
        elif s == "do()":
            enabled = True
        else:
            if enabled:
                num_a, num_b = [int(n) for n in s[4:-1].split(",")]
                res += (num_a * num_b)
    
    print(f"With conditionals: {res}")


def find_and_multiply(string: str):
    li = re.findall(r'mul\(\d+,\d+\)', string)

    res = 0

    for s in li:
        num_a, num_b = [int(n) for n in s[4:-1].split(",")]
        res += (num_a * num_b)

    print(res)

def main():
    
    input_file = 'input.txt'

    with open(input_file, 'r') as f:
        string = f.read()

    find_and_multiply(string)

    find_and_multiply_with_cond(string)
   


if __name__ == '__main__':
    main()