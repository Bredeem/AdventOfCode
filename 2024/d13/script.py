import re
import numpy as np
# INPUT_FILE = "input.txt"
INPUT_FILE = "test_input.txt"

def part1(configs: dict[list[list[int]]]):
    pass    

def part2():
    pass

def main():
    
    configs = []

    with open(INPUT_FILE, "r") as f:
        for config in f.read().strip().split("\n\n"):
            print(config)
            d = {}
            a, b, prize = config.split("\n")

            

            d["A"] = [[int(a.split()[2][2:-1]), int(a.split()[3][2:])],[int(b.split()[2][2:-1]), int(b.split()[3][2:])]]
            d["b"] = [int(prize.split()[1][2:-1]), int(prize.split()[2][2:])]
            
            configs.append(d)
    
    part1(configs)


if __name__ == '__main__':
    main()