INPUT_FILE = "input.txt"
# INPUT_FILE = "test_input.txt"


def explore_path(pos: str, input_dict: dict):
    if pos == "out":
        return 1

    new_paths = input_dict[pos]
    sum = 0
    for path in new_paths:
        sum += explore_path(path, input_dict)
    return sum


def part1(input_dict: dict):

    n_paths = explore_path("you", input_dict)

    print(f"Part 1: {n_paths}")


def paths_to_elem(
    pos: str, goal: str, input_dict: dict, explored_paths: dict, banned: str
):
    if pos in explored_paths.keys():
        return explored_paths[pos]

    if pos == goal:
        explored_paths[pos] = 1
        return explored_paths[pos]
    elif pos == banned or pos == "out":
        explored_paths[pos] = 0
        return explored_paths[pos]

    new_paths = input_dict[pos]
    sum = 0
    for path in new_paths:
        sum += paths_to_elem(path, goal, input_dict, explored_paths, banned)
    explored_paths[pos] = sum
    return explored_paths[pos]


def part2(input_dict: dict):
    svr_to_fft = paths_to_elem("svr", "fft", input_dict, {}, "dac")
    fft_to_dac = paths_to_elem("fft", "dac", input_dict, {}, "")
    dac_to_out = paths_to_elem("dac", "out", input_dict, {}, "fft")

    svr_to_dac = paths_to_elem("svr", "dac", input_dict, {}, "fft")
    dac_to_fft = paths_to_elem("dac", "fft", input_dict, {}, "")
    fft_to_out = paths_to_elem("fft", "out", input_dict, {}, "dac")

    # print(svr_to_fft, fft_to_dac, dac_to_out)
    # print(svr_to_dac, dac_to_fft, fft_to_out)

    n_paths = (svr_to_fft * fft_to_dac * dac_to_out) + (
        svr_to_dac * dac_to_fft * fft_to_out
    )
    print(f"Part 2: {n_paths}")


def main():
    with open(INPUT_FILE, "r") as f:
        input_string = f.read()

    input_dict = {}
    for l in input_string.splitlines():
        parts = l.split(" ")
        input_dict[parts[0][:-1]] = parts[1:]

    part1(input_dict)
    part2(input_dict)


if __name__ == "__main__":
    main()
