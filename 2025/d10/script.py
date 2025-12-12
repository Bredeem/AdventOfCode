import heapq
import math
from itertools import combinations_with_replacement
from pprint import pprint

INPUT_FILE = "input.txt"
# INPUT_FILE = "test_input.txt"


def find_diagram(entry):
    goal = [i == "#" for i in entry["diagram"]]
    n_indicators = len(goal)
    n_presses = 1
    while True:
        for buttons in combinations_with_replacement(entry["buttons"], n_presses):
            indicators = [False for _ in range(n_indicators)]
            for button in buttons:
                for i in button:
                    indicators[i] = not indicators[i]
            if indicators == goal:
                return n_presses
        n_presses += 1


def part1(manual: list[dict]):
    sum = 0

    for entry in manual:
        sum += find_diagram(entry)

    print(f"Part 1: {sum}")


def calculate_heuristic(current_state, goal, max_effect_value):
    R_total = sum(goal[i] - current_state[i] for i in range(len(goal)))

    if R_total == 0:
        return 0

    # max_effect_value is the max number of 1s in any button (pre-calculated once)
    # Ceiling division: math.ceil(R_total / max_effect_value)
    return math.ceil(R_total / max_effect_value)


def find_joltage(entry):
    goal = tuple(int(i) for i in entry["joltage"])
    n_counters = len(goal)

    buttons_effects = []
    max_effect_value = 0
    for button_indices in entry["buttons"]:
        effect = [0] * n_counters
        current_effect_sum = 0
        for index in button_indices:
            effect[index] += 1
            current_effect_sum += 1
        buttons_effects.append(tuple(effect))
        max_effect_value = max(max_effect_value, current_effect_sum)

    start_state = tuple([0] * n_counters)
    g_score = {start_state: 0}

    h_start = calculate_heuristic(start_state, goal, max_effect_value)
    f_start = h_start

    queue = [(f_start, 0, start_state)]
    while queue:
        f_cur, g_cur, cur_state = heapq.heappop(queue)

        if cur_state == goal:
            print(f"Number of presses:", g_cur)
            return g_cur

        if g_cur > g_score.get(cur_state, float("inf")):
            continue

        for effect in buttons_effects:
            next_state_list = list(cur_state)

            exceded = False
            for i in range(n_counters):
                next_state_list[i] += effect[i]
                if next_state_list[i] > goal[i]:
                    exceded = True
                    break

            if not exceded:
                next_state = tuple(next_state_list)
                g_next = g_cur + 1

                if g_next < g_score.get(next_state, float("inf")):
                    g_score[next_state] = g_next
                    h_next = calculate_heuristic(next_state, goal, max_effect_value)
                    f_next = g_next + h_next
                    heapq.heappush(queue, (f_next, g_next, next_state))

    print("Something is wrong, I can feel it...")
    return -1


def part2(manual):
    sum = 0

    for i, entry in enumerate(manual, 1):
        print(f"Entry {i} of {len(manual)}")
        sum += find_joltage(entry)

    print(f"Part 2: {sum}")


def main():
    with open(INPUT_FILE, "r") as f:
        input_string = f.read()

    manual = []
    for l in input_string.splitlines():
        entry = dict()
        parts = l.split(" ")
        entry["diagram"] = list(parts[0][1:-1])
        entry["buttons"] = [list(map(int, b[1:-1].split(","))) for b in parts[1:-1]]
        entry["joltage"] = parts[-1][1:-1].split(",")
        manual.append(entry)

    # pprint(manual)

    part1(manual)
    part2(manual)


if __name__ == "__main__":
    main()
