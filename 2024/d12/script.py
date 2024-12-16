
# INPUT_FILE = "small_test_input.txt"
# INPUT_FILE = "big_test_input.txt"
# INPUT_FILE = "e_input.txt"
INPUT_FILE = "input.txt"

DIRS = [(-1,0), (0,1), (1,0), (0,-1)]
dir_names = {
    (-1,0): "up",
    (0,1): "right",
    (1,0): "down",
    (0,-1): "left"
}

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
    invalid_dirs = []

    for dir in DIRS:
        step = add_vecs(pos, dir)
        if in_bounds(step, R, C) and map[step[0]][step[1]] == map[pos[0]][pos[1]]:
            valid_steps.append(step)
        else:
            invalid_dirs.append(dir)
    return valid_steps, invalid_dirs

def find_fence_info(map: list[list[str]], pos: tuple[int], visited: set):
    area = 0
    perimiter = 0

    not_visited = set()
    not_visited.add(pos)

    region = {}


    # While there are yet to be visited locations or there is no visited locations yet
    while not_visited:
        cur_pos = not_visited.pop()
        valid_steps, invalid_dirs = check_around(map, cur_pos)
        for step in valid_steps:
            if step not in visited: 
                not_visited.add(step) 
        
        area += 1
        perimiter += 4-len(valid_steps)

        # print(f"{cur_pos=}")           
        visited.add(cur_pos)
        region[cur_pos] = invalid_dirs 


    # print(f"Region {map[pos[0]][pos[1]]}:")
    # print(f"{area=}, {perimiter=}")
    return area, perimiter, region

def find_neighbors(region: dict[tuple[int, int]: list[int]], pos: tuple[int, int], dir: tuple[int, int]):
    
    neighbors = []

    i = 1
    n_r = None
    n_l = None
    if dir in [(1,0), (-1,0)]:
        while True:
            pos_r = add_vecs(pos, (0, i))
            n_r = region.get(pos_r)
            if n_r and dir in n_r:
                neighbors.append(pos_r)
            else:
                break
            i += 1

        i = 1
        while True:

            pos_l = add_vecs(pos, (0, -i))
            n_l = region.get(pos_l)

            if n_l and dir in n_l:
                neighbors.append(pos_l)
            else:
                break
            i += 1    

    else:
        while True:
            pos_d = add_vecs(pos, (i, 0))
            n_d = region.get(pos_d)
            if n_d and dir in n_d:
                neighbors.append(pos_d)
            else:
                break
            i += 1

        i = 1
        while True:

            pos_u = add_vecs(pos, (-i, 0))
            n_u = region.get(pos_u)

            if n_u and dir in n_u:
                neighbors.append(pos_u)
            else:
                break
            i += 1   

    return neighbors


def find_sides(region: dict[tuple[int, int]: list[int]]):
    
    sides = {
        (-1,0): [],
        (0,1): [],
        (1,0): [],
        (0,-1): []
    }

    for pos in region.keys():
        for dir in region[pos]:
            if not any(pos in l for l in sides[dir]):
                neighbors = find_neighbors(region, pos, dir)
                sides[dir].append(neighbors)


    # print(sides)

    # for k, v in sides.items():
    #     print(dir_names[k])
    #     print(v)
    #     print(len(v))

    num_sides = sum(len(s) for s in sides.values())
    # print(f"{num_sides=}")
            
    return num_sides





def solve(map: list[list[str]]):
    visited = set()

    R = len(map)
    C = len(map[0])

    part_one = 0
    part_two = 0

    for r in range(R):
        for c in range(C):
           if (r,c) not in visited:
                # print(map[r][c])
                area, perim, reg = find_fence_info(map, (r,c), visited)
                # print(f"{area=}, {perim=}")

                part_one += area * perim
                
                sides = find_sides(reg)
                part_two += area * sides


    print(f"Part 1: {part_one}")
    print(f"Part 2: {part_two}")



def main():
    
    arr = []

    with open(INPUT_FILE, "r") as f:
        for line in f.read().split():
            arr.append([c for c in line])


    solve(arr)

if __name__ == '__main__':
    main()