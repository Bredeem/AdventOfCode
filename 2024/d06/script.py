from multiprocessing import Pool
from functools import partial

INPUT_FILE = "input.txt"

# up, left, down, right
DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

def in_bounds(pos: tuple[int], rows: int, cols: int) -> bool:
    if 0 <= pos[0] and pos[0] < rows and 0 <= pos[1] and pos[1] < cols:
        return True
    return False

def add_vecs(vec1: tuple[int], vec2: tuple[int]) -> tuple[int]:
    return (vec1[0] + vec2[0], vec1[1] + vec2[1]) 

def part1(arr: list[list[str]]):
    for line in arr:
        if "^" in line:
            guard_pos = (arr.index(line), line.index("^"))

    R = len(arr)
    C = len(arr[0])

    cur_dir = 0

    visited = set()
    while in_bounds(guard_pos, R, C):
        step_ahead = add_vecs(guard_pos, DIRS[cur_dir])
        if in_bounds(step_ahead, R, C):
            if arr[step_ahead[0]][step_ahead[1]] == "#":
                cur_dir = (cur_dir + 1) % 4
                continue

        visited.add(guard_pos)
        guard_pos = step_ahead


    print(f"Part 1: {len(visited)}")

    return visited

def check_if_infinite_loop(new_obs_pos, arr, start_pos):
    if new_obs_pos == start_pos:
        return False

    guard_steps = []

    R = len(arr)
    C = len(arr[0])

    cur_dir = 0

    guard_pos = start_pos
    while in_bounds(guard_pos, R, C):
        step_ahead = add_vecs(guard_pos, DIRS[cur_dir])
        if in_bounds(step_ahead, R, C):
            if arr[step_ahead[0]][step_ahead[1]] == "#" or step_ahead == new_obs_pos:
                if {"pos": guard_pos, "dir": cur_dir} in guard_steps:
                    return True
                guard_steps.append({"pos": guard_pos, "dir": cur_dir})
                cur_dir = (cur_dir + 1) % 4
                
                continue

        guard_pos = step_ahead

    return False


def part2(arr: list[list[str]], visited: set[tuple[int]]):
    
    R = len(arr)
    C = len(arr[0])

    for line in arr:
        if "^" in line:
            guard_pos = (arr.index(line), line.index("^"))
    
    res = 0

    with Pool() as pool:
        res = pool.map(partial(check_if_infinite_loop, arr=arr, start_pos=guard_pos), visited)

    # for cords in visited:
    #     if check_if_infinite_loop(cords, arr, guard_pos):
    #         res += 1
    # print(f"Part 2: {res}")
    print(f"Part 2: {sum(res)}")



def main():
    
    with open(INPUT_FILE, "r") as f:
        input_string = f.read().strip()

    input_arr = []
    for line in input_string.split("\n"):
        input_arr.append([c for c in line.strip()]) 


    visited = part1(input_arr)
    part2(input_arr, visited)

if __name__ == '__main__':
    main()