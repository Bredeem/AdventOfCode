
INPUT_FILE = "input.txt"

DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

def add_vecs(vec1: tuple[int], vec2: tuple[int]) -> tuple[int]:
    return (vec1[0] + vec2[0], vec1[1] + vec2[1]) 

def in_bounds(pos: tuple[int], rows: int, cols: int) -> bool:
    if 0 <= pos[0] and pos[0] < rows and 0 <= pos[1] and pos[1] < cols:
        return True
    return False

def _find_tops(map: list[list[str]], pos: tuple[int], cur_height: int, tops: set, trails: list, R: int, C: int):
    if cur_height == 9:
        tops.add(pos)
        trails.append(pos)
        return

    for dir in DIRS:
        new_pos = add_vecs(pos, dir)
        if not in_bounds(new_pos, R, C):
            continue

        new_height = int(map[new_pos[0]][new_pos[1]])
        if new_height == cur_height + 1:
            _find_tops(map, new_pos, new_height, tops, trails, R, C)    

def find_score(map: list[list[str]], start: tuple[int], R: int, C: int):

    trails = list()
    tops = set()
    _find_tops(map, start, 0, tops, trails, R, C)
    return len(tops), len(trails)



def solution(map: list[list[str]]):
    R = len(map)
    C = len(map[0])
    
    p1_score = 0
    p2_score = 0
    for r in range(R):
        for c in range(C):
            if map[r][c] == "0":
                p1, p2 = find_score(map, (r, c), R, C)
                p1_score += p1
                p2_score += p2

    print(f"Part 1: {p1_score}")
    print(f"Part 2: {p2_score}")

def main():
    
    with open(INPUT_FILE, "r") as f:
        input_array  = [[c for c in line.strip()] for line in f.readlines()]

    # for line in input_array:
    #     print(line)

    solution(input_array)

if __name__ == '__main__':
    main()