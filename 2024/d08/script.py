
INPUT_FILE = "input.txt"


def add_vecs(vec1: tuple[int], vec2: tuple[int]) -> tuple[int]:
    return (vec1[0] + vec2[0], vec1[1] + vec2[1]) 

def in_bounds(pos: tuple[int], rows: int, cols: int) -> bool:
    if 0 <= pos[0] and pos[0] < rows and 0 <= pos[1] and pos[1] < cols:
        return True
    return False

def find_antinodes(map: list[str], c: str, pos: tuple[int], R: int, C: int):
    
    antinodes = set()
    
    for i in range(R):
        for j in range(C):
            other_c = map[i][j]
            if other_c == c and (i, j) != pos:
                
                # print(f"{c=}, {pos=}")
                # print(f"{other_c=}, {(i,j)}")

                dist = add_vecs(pos, (-i,-j))
                # print(f"{dist=}")
                ant_a = add_vecs(pos, dist)
                ant_b = add_vecs((i,j), (-dist[0], -dist[1]))

                # print(f"{ant_a}, {ant_b}")
                # print()
                if in_bounds(ant_a, R, C):
                    antinodes.add(ant_a)
                if in_bounds(ant_b, R, C):
                    antinodes.add(ant_b)
    
    return antinodes


def part1(map: list[str]):
    R = len(map)
    C = len(map[0])

    antidotes = set()

    for i in range(len(map)):
        for j in range(len(map[i].strip())):
            if map[i][j] != ".":
                ads = find_antinodes(map, map[i][j], (i, j), R, C)
                antidotes.update(ads)


    # print(antidotes)
    # for ant in antidotes:
    #     if map[ant[0]][ant[1]] == ".":
            
    #         map[ant[0]] = map[ant[0]][:ant[1]] + "#" + map[ant[0]][ant[1]+1:]
    
    # for line in map:
    #     print(line)

    print(f"Part 1: {len(antidotes)}")

def find_all_antinodes(map: list[str], c: str, pos: tuple[int], R: int, C: int):
    antinodes = set()
    
    for i in range(R):
        for j in range(C):
            other_c = map[i][j]
            if other_c == c and (i, j) != pos:
                dist = add_vecs(pos, (-i,-j))

                node = pos
                while in_bounds(node, R, C):
                    antinodes.add(node)
                    node = add_vecs(node, dist)
    
    return antinodes


def part2(map: list[str]):
    R = len(map)
    C = len(map[0])

    antidotes = set()

    for i in range(len(map)):
        for j in range(len(map[i].strip())):
            if map[i][j] != ".":
                ads = find_all_antinodes(map, map[i][j], (i, j), R, C)
                antidotes.update(ads)

    print(f"Part 2: {len(antidotes)}")


def main():
    
    with open(INPUT_FILE, "r") as f:
        map = [line.strip() for line in f.readlines()]

    part1(map)
    part2(map)

if __name__ == '__main__':
    main()