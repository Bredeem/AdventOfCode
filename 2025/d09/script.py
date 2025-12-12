from functools import partial
from itertools import combinations
from multiprocessing import Pool

INPUT_FILE = "input.txt"
# INPUT_FILE = "test_input.txt"


def part1(cords: list[tuple[int, int]]):
    largest_area = 0
    for (x1, y1), (x2, y2) in combinations(cords, 2):
        x_len = max(x1, x2) - min(x1, x2) + 1
        y_len = max(y1, y2) - min(y1, y2) + 1

        area = x_len * y_len
        largest_area = max(largest_area, area)

    print(f"Part 1: {largest_area}")


def print_grid(grid: list[list[str]]):
    for row in grid:
        print("".join(row))
    print()


def in_bounds(x1: int, y1: int, x2: int, y2: int, cords: list[tuple[int, int]]):
    n = len(cords)
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            inside = False
            for i in range(n):
                px1, py1 = cords[i]
                px2, py2 = cords[(i + 1) % n]

                if min(py1, py2) < y <= max(py1, py2):
                    x_intersect = px1 + (y - py1) * (px2 - px1) / (py2 - py1)
                    if x < x_intersect:
                        inside = not inside
            if not inside:
                return False
    return True


def worker(args, cords):
    x1, y1 = args[0]
    x2, y2 = args[1]
    if not in_bounds(x1, y1, x2, y2, cords):
        return None

    x_len = max(x1, x2) - min(x1, x2) + 1
    y_len = max(y1, y2) - min(y1, y2) + 1

    return x_len * y_len


def part2(cords: list[tuple[int, int]]):
    largest_area = 0

    with Pool() as pool:
        res = pool.map(partial(worker, cords=cords), combinations(cords, 2))

    largest_area = max([r for r in res if r])

    print(f"Part 2: {largest_area}")


def main():
    with open(INPUT_FILE, "r") as f:
        input_lines = f.read().splitlines()

    cords = [(int(l.split(",")[0]), int(l.split(",")[1])) for l in input_lines]

    part1(cords)
    part2(cords)


if __name__ == "__main__":
    main()
