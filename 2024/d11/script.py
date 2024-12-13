from functools import reduce
from operator import iconcat

INPUT_FILE = "input.txt"

BLINKS = 6

cache = {}

def apply_rules(n: str):
    if not cache.get(n):
        if len(n) % 2 == 0:
            cache[n] = (n[:len(n)//2], n[len(n)//2:])
        else:
            cache[n] = str(int(n)*2024)

    return cache[n]

def _recurse(blinks: int, n: str):
    if blinks >= BLINKS:
        return 1

    if (n, blinks) in cache:
        return cache[(n, blinks)]
    

    if n == "0":
        cache[(n, blinks)] = _recurse(blinks+1, "1")
    elif (l := len(n)) % 2 == 0:
        cache[(n, blinks)] = _recurse(blinks+1, n[:l//2]) + _recurse(blinks+1, n[l//2:])
    else:
        cache[(n, blinks)] = _recurse(blinks+1, str(n*2024))
    return cache[(n, blinks)]

    # new_num = apply_rules(num)
    # if type(new_num) == tuple:
    #     return _recurse(blinks+1, new_num[0]) + _recurse(blinks+1, new_num[1])
    # else:
    #     return _recurse(blinks+1, new_num)


def part2(stones: list[str]):
    res = 0

    for i, stone in enumerate(stones, 1):
        res += _recurse(0, stone)
        print(f"{12.5 * i:.1f}% done...")
    
    print("Part 2:")
    print(f"{res} stones after {BLINKS} blinks.")
    


def main():
    
    with open(INPUT_FILE, "r") as f:
        input_list = f.read().split()
    
    # part1(input_list)
    part2(input_list)


if __name__ == '__main__':
    main()