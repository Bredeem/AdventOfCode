INPUT_FILE = "input.txt"
# INPUT_FILE = "test_input.txt"


def n_boxes_around(grid: list[list[str]], pos: tuple[int, int], h: int, w: int):
    n = 0
    i, j = pos
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue

            if (0 <= i + x < h) and (0 <= j + y < w):
                if grid[i + x][j + y] == "@":
                    n += 1
    return n


def part1(grid: list[list[str]]):
    rolls = 0
    h = len(grid)
    w = len(grid[0])

    for i in range(h):
        for j in range(w):
            if grid[i][j] == "@" and n_boxes_around(grid, (i, j), h, w) < 4:
                rolls += 1

    print(f"Part 1: Accessable rolls of paper is {rolls}")


def part2(grid: list[list[str]]):
    rolls = 0
    h = len(grid)
    w = len(grid[0])

    while True:
        cords = set()
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "@" and n_boxes_around(grid, (i, j), h, w) < 4:
                    cords.add((i, j))
                    rolls += 1

        if len(cords) == 0:
            break
        for i, j in cords:
            grid[i][j] = "x"

    print(f"Part 2: Accessable rolls of paper is {rolls}")


def main():

    with open(INPUT_FILE, "r") as f:
        input_grid = [[c for c in line] for line in f.read().splitlines()]

    # print(input_grid)
    part1(input_grid)
    part2(input_grid)


if __name__ == "__main__":
    main()
