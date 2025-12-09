INPUT_FILE = "input.txt"
# INPUT_FILE = "test_input.txt"


def print_grid(grid: list[list[str]]):
    for row in grid:
        print("".join(row))
    print()


def part1(grid: list[list[str]]):
    splits = 0
    beam_idxs = set([grid[0].index("S")])
    for row in grid[1:]:
        new_beam_idxs = set()
        for idx in beam_idxs:
            if row[idx] == "." or row[idx] == "|":
                # row[idx] = "|"
                new_beam_idxs.add(idx)
            elif row[idx] == "^":
                # row[idx - 1] = "|"
                # row[idx + 1] = "|"
                new_beam_idxs.add(idx - 1)
                new_beam_idxs.add(idx + 1)
                splits += 1
            else:
                print(f"Unexpected character: {row[idx]}")
                exit()
        beam_idxs = new_beam_idxs
        # print_grid(grid)

    print(f"Part 1: {splits}")


def check_path(grid: list[list[str]], explored_paths: dict, row_idx: int, col_idx: int):
    path_key = (row_idx, col_idx)

    if path_key in explored_paths.keys():
        return explored_paths[path_key]

    if row_idx == len(grid):
        explored_paths[path_key] = 1
        return explored_paths[path_key]

    if grid[row_idx][col_idx] == "^":
        explored_paths[path_key] = check_path(
            grid, explored_paths, row_idx, col_idx - 1
        ) + check_path(grid, explored_paths, row_idx, col_idx + 1)
        return explored_paths[path_key]

    if grid[row_idx][col_idx] == ".":
        explored_paths[path_key] = check_path(
            grid, explored_paths, row_idx + 1, col_idx
        )
        return explored_paths[path_key]

    print(f"Unexpected character: {grid[row_idx][col_idx]}")
    exit()


def part2(grid: list[list[str]]):
    # print_grid(grid)
    start_idx = grid[0].index("S")
    explored_paths = {}

    timelines = check_path(grid, explored_paths, 1, start_idx)

    print(f"Part 2: {timelines}")


def main():
    with open(INPUT_FILE, "r") as f:
        input_grid = [[c for c in line] for line in f.read().splitlines()]

    part1(input_grid.copy())
    part2(input_grid.copy())


if __name__ == "__main__":
    main()
