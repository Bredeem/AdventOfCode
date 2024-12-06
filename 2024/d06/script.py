import copy
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

    while in_bounds(guard_pos, R, C):
        step_ahead = add_vecs(guard_pos, DIRS[cur_dir])
        if in_bounds(step_ahead, R, C):
            if arr[step_ahead[0]][step_ahead[1]] == "#":
                cur_dir = (cur_dir + 1) % 4
                continue

        arr[guard_pos[0]][guard_pos[1]] = "X"
        guard_pos = step_ahead


    res = 0
    for line in arr:
        res += line.count("X")
    print(f"Part 1: {res}")

    return res

def check_if_infinite_loop(arr, start_pos, new_obs_pos):
    if new_obs_pos == start_pos:
        return False
    
    arr = copy.deepcopy(arr)

    guard_steps = []

    arr[new_obs_pos[0]][new_obs_pos[1]] = "#"

    R = len(arr)
    C = len(arr[0])

    cur_dir = 0

    guard_pos = start_pos
    while in_bounds(guard_pos, R, C):
        step_ahead = add_vecs(guard_pos, DIRS[cur_dir])
        if in_bounds(step_ahead, R, C):
            if arr[step_ahead[0]][step_ahead[1]] == "#":
                cur_dir = (cur_dir + 1) % 4
                continue

        if {"pos": guard_pos, "dir": cur_dir} in guard_steps:
            return True
        
        guard_steps.append({"pos": guard_pos, "dir": cur_dir})

        guard_pos = step_ahead


    return False

    
def worker(i, arr, path_arr, guard_pos):
    res = 0
    for j in range(len(arr[0])):
        if path_arr[i][j] == "X":
            if check_if_infinite_loop(arr, guard_pos, (i,j)):
                res += 1
    
    return res


def part2(arr: list[list[str]], path_arr: list[list[str]], num_checks):
    
    R = len(arr)
    C = len(arr[0])

    for line in arr:
        if "^" in line:
            guard_pos = (arr.index(line), line.index("^"))
    
    with Pool() as pool:
        res = pool.map(partial(worker, arr=arr, path_arr=path_arr, guard_pos=guard_pos ), range(R))

    print(f"Part 2: {sum(res)}")



def main():
    
    with open(INPUT_FILE, "r") as f:
        input_string = f.read().strip()

    arr_1 = []
    arr_2 = []
    for line in input_string.split("\n"):
        arr_1.append([c for c in line.strip()]) 
        arr_2.append([c for c in line.strip()]) 


    num = part1(arr_1)
    part2(arr_2, arr_1, num)

if __name__ == '__main__':
    main()