import numpy as np

# INPUT_FILE = "small_test_input.txt"
# INPUT_FILE = "big_test_input.txt"
INPUT_FILE = "input.txt"

DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

def add_vecs(vec1: tuple[int], vec2: tuple[int]) -> tuple[int]:
    return (vec1[0] + vec2[0], vec1[1] + vec2[1]) 

def in_bounds(pos: tuple[int], R: int, C: int):
    if 0 <= pos[0] and pos[0] < R and 0 <= pos[1] and pos[1] < C:
        return True
    return False

def check_around(map: list[list[str]], pos: tuple[int]):
    R = len(map)
    C = len(map[0])

    valid_steps = []

    for dir in DIRS:
        step = add_vecs(pos, dir)
        if in_bounds(step, R, C) and map[step[0]][step[1]] == map[pos[0]][pos[1]]:
            valid_steps.append(step)
            
    return valid_steps

def find_fence_price(map: list[list[str]], pos: tuple[int], visited: set):
    area = 0
    perimiter = 0

    not_visited = set()

    not_visited.add(pos)

    # While there are yet to be visited locations or there is no visited locations yet
    while not_visited:
        cur_pos = not_visited.pop()
        valid_steps = check_around(map, cur_pos)
        for step in valid_steps:
            if step not in visited: 
                not_visited.add(step) 
        
        area += 1
        perimiter += 4-len(valid_steps)

        visited.add(cur_pos)
        
    # print(f"Region {map[pos[0]][pos[1]]}:")
    # print(f"{area=}, {perimiter=}")
    return area * perimiter


def part1(map: list[list[str]]):
    visited = set()

    R = len(map)
    C = len(map[0])

    res = 0

    for r in range(R):
        for c in range(C):
           if (r,c) not in visited:
               res += find_fence_price(map, (r,c), visited)
                
    print(f"Part 1: {res}")





def part2():
    pass

def main():
    
    arr = []

    with open(INPUT_FILE, "r") as f:
        for line in f.read().split():
            arr.append([c for c in line])


    part1(arr)

if __name__ == '__main__':
    main()