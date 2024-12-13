INPUT_FILE = "input.txt"

BLINKS = 75

cache = {}

def _recurse(blinks: int, n: int):
    if blinks == BLINKS:
        return 1

    if (n, blinks) in cache:
        return cache[(n, blinks)]
    
    if n == 0:
        cache[(n, blinks)] = _recurse(blinks+1, 1)
    elif (l := len(str(n))) % 2 == 0:
        cache[(n, blinks)] = _recurse(blinks+1, int(str(n)[:l//2])) + _recurse(blinks+1, int(str(n)[l//2:]))
    else:
        cache[(n, blinks)] = _recurse(blinks+1, n*2024)
    return cache[(n, blinks)]

def part2(stones: list[int]):
    res = 0

    for stone in stones:
        res += _recurse(0, stone)
    
    print("Part 2:")
    print(f"{res} stones after {BLINKS} blinks.")
    


def main():
    
    with open(INPUT_FILE, "r") as f:
        input_list = [int(n) for n in f.read().split()]
    part2(input_list)

if __name__ == '__main__':
    main()