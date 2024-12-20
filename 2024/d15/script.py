
# INPUT_FILE = "input.txt"
INPUT_FILE = "test_input.txt"
# INPUT_FILE = "small_test_input.txt"
# INPUT_FILE = "other_test_input.txt"


def find_start(warehouse: list[list[str]]) -> tuple[int, int]:
    for i, row in enumerate(warehouse):
        for j, element in enumerate(row):
            if element == "@":
                return (i, j)
    return None


def move(warehouse: list[list[str]], cur_pos: tuple[int, int], direction: str) -> tuple[int, int]:
    i, j = cur_pos
    
    if direction == "<":
        while warehouse[i][j] != "#":
            j -= 1
            if warehouse[i][j] == ".":
                for j in range(j, cur_pos[1]):
                    warehouse[i][j] = warehouse[i][j+1]
                warehouse[cur_pos[0]][cur_pos[1]] = "."
                return (i, j)
        return cur_pos
    
    elif direction == ">":
        while warehouse[i][j] != "#":
            j += 1
            if warehouse[i][j] == ".":
                for j in range(j, cur_pos[1], -1):
                    warehouse[i][j] = warehouse[i][j-1]
                warehouse[cur_pos[0]][cur_pos[1]] = "."
                return (i, j)
        return cur_pos
    
    elif direction == "^":
        while warehouse[i][j] != "#":
            i -= 1
            if warehouse[i][j] == ".":
                for i in range(i, cur_pos[0]):
                    warehouse[i][j] = warehouse[i+1][j]
                warehouse[cur_pos[0]][cur_pos[1]] = "."
                return (i, j)
        return cur_pos
    
    else:
        while warehouse[i][j] != "#":
            i += 1
            if warehouse[i][j] == ".":
                for i in range(i, cur_pos[0], -1):
                    warehouse[i][j] = warehouse[i-1][j]
                warehouse[cur_pos[0]][cur_pos[1]] = "."
                return (i, j)
        return cur_pos
    


def part1(warehouse: list[list[str]], directions: str):
    for line in warehouse:
        print("".join(line))
    print()
    cur_pos = find_start(warehouse)

    for direction in directions:
        cur_pos = move(warehouse, cur_pos, direction)
        # print(f"Move {direction}:")
        # for line in warehouse:
        #     print("".join(line))
        # print()

    for line in warehouse:
        print("".join(line))
    print()


    res = 0
    for i, line in enumerate(warehouse):
        for j, c in enumerate(line):
            if c == "O":
                res += (100 * i) + j

    print("Part 1:", res)


def double_warehouse(warehouse: list[list[str]]) -> list[list[str]]:
    new_warehouse = []
    
    for line in warehouse:
        new_line = []
        for c in line:
            if c == "#":
                new_line += ["#", "#"]
            elif c == "O":
                new_line += ["[", "]"]
            elif c == ".":
                new_line += [".", "."]
            else:
                new_line += ["@", "."]
        new_warehouse.append(new_line)
    

    return new_warehouse



def move_big(warehouse: list[list[str]], cur_pos: tuple[int, int], direction: str) -> tuple[int, int]:
    i, j = cur_pos

    if direction == "<":
        while warehouse[i][j] != "#":
            j -= 1
            if warehouse[i][j] == ".":
                for j in range(j, cur_pos[1]):
                    warehouse[i][j] = warehouse[i][j+1]
                warehouse[cur_pos[0]][cur_pos[1]] = "."
                return (i, j)
        return cur_pos  
    elif direction == ">":
        while warehouse[i][j] != "#":
            j += 1
            if warehouse[i][j] == ".":
                for j in range(j, cur_pos[1], -1):
                    warehouse[i][j] = warehouse[i][j-1]
                warehouse[cur_pos[0]][cur_pos[1]] = "."
                return (i, j)
        return cur_pos
    elif direction == "^":
        boxes_to_move = set()
        cols_to_check = set([j])
        while not any([warehouse[i][col] == "#" for col in cols_to_check]):
            i -= 1
            new_cols = set()
            for col in cols_to_check:
                if warehouse[i][col] == "[":
                    new_cols.add(col+1)
                    boxes_to_move.update([(i, col), (i, col+1)])
                elif warehouse[i][col] == "]":
                    new_cols.add(col-1)
                    boxes_to_move.update([(i, col), (i, col-1)])
            cols_to_check.update(new_cols)
            if all([warehouse[i][col] == "." for col in cols_to_check]):
                for i in range(i, cur_pos[0]):
                    for col in cols_to_check:
                        if (i, col) in boxes_to_move:
                            warehouse[i-1][col] = warehouse[i][col]
                            warehouse[i][col] = "."
                warehouse[cur_pos[0]][cur_pos[1]] = "."
                warehouse[i][j] = "@"
                return (i, j)
        return cur_pos
    else:
        boxes_to_move = set()
        cols_to_check = set([j])
        while not any([warehouse[i][col] == "#" for col in cols_to_check]):
            i += 1
            new_cols = set()
            for col in cols_to_check:
                if warehouse[i][col] == "[":
                    new_cols.add(col+1)
                    boxes_to_move.update([(i, col), (i, col+1)])
                elif warehouse[i][col] == "]":
                    new_cols.add(col-1)
                    boxes_to_move.update([(i, col), (i, col-1)])
            cols_to_check.update(new_cols)
            if all([warehouse[i][col] == "." for col in cols_to_check]):
                for i in range(i, cur_pos[0], -1):
                    for col in cols_to_check:
                        if (i, col) in boxes_to_move:
                            warehouse[i+1][col] = warehouse[i][col]
                            warehouse[i][col] = "."
                warehouse[cur_pos[0]][cur_pos[1]] = "."
                warehouse[i][j] = "@"
                return (i, j)
        return cur_pos


def part2(warehouse: list[list[str]], directions: str):
    warehouse = double_warehouse(warehouse)
    for line in warehouse:
        print("".join(line))
    print()

    cur_pos = find_start(warehouse)

    for direction in directions:
        cur_pos = move_big(warehouse, cur_pos, direction)
        # print(f"Move {direction}:")
        # for line in warehouse:
        #     print("".join(line))
        # print()

    for line in warehouse:
        print("".join(line))
    print()


    res = 0
    for i, line in enumerate(warehouse):
        for j, c in enumerate(line):
            if c == "[":
                res += (100 * i) + j

    print("Part 2:", res)

def main():
    
    warehouse = []

    with open(INPUT_FILE, "r") as f:
        m, d = f.read().strip().split("\n\n")
        
        for line in m.split("\n"):
            warehouse.append([c for c in line])

        d = d.replace("\n", "")

    # part1(warehouse, d)
    part2(warehouse, d)

if __name__ == '__main__':
    main()