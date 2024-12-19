import time

INPUT_FILE = "input.txt"
# INPUT_FILE = "test_input.txt"

# ROOM_SIZE = (11, 7)
ROOM_SIZE = (101, 103)


def part1(robots: list[dict]):
    m = [['.' for _ in range(ROOM_SIZE[0])] for _ in range(ROOM_SIZE[1])]

    quadrants = [0,0,0,0]

    for robot in robots:
        new_x = (robot["p"][0] + (robot["v"][0] * 100)) % ROOM_SIZE[0]
        new_y = (robot["p"][1] + (robot["v"][1] * 100)) % ROOM_SIZE[1]
        
        # print(robot["p"], robot["v"])
        # print(new_x, new_y)


        if m[new_y][new_x] == ".":
            m[new_y][new_x] = "1"
        else:
            m[new_y][new_x] = str(int(m[new_y][new_x]) + 1)
    
        if new_x < ROOM_SIZE[0] // 2 and new_y < ROOM_SIZE[1] // 2:
            quadrants[0] += 1
        elif new_x > ROOM_SIZE[0] // 2 and new_y < ROOM_SIZE[1] // 2:
            quadrants[1] += 1
        elif new_x < ROOM_SIZE[0] // 2 and new_y > ROOM_SIZE[1] // 2:
            quadrants[2] += 1
        elif new_x > ROOM_SIZE[0] // 2 and new_y > ROOM_SIZE[1] // 2:
            quadrants[3] += 1

    for line in m:
        print("".join(line))   

    res = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

    print(f"Part 1: {res}")
    
    



def part2(robots: list[dict]):

    seconds = 0

    while True:
        m = [['.' for _ in range(ROOM_SIZE[0])] for _ in range(ROOM_SIZE[1])]
        print("\033c", end="")

        for robot in robots:
            new_x = (robot["p"][0] + robot["v"][0]) % ROOM_SIZE[0]
            new_y = (robot["p"][1] + robot["v"][1]) % ROOM_SIZE[1]
            robot["p"] = [new_x, new_y]

        
            m[new_y][new_x] = "#"

        seconds += 1

        for line in m:
            if "###########" in "".join(line):
                print(f"Seconds: {seconds}")
                for line in m:
                    print("".join(line))
                return seconds


def main():
    
    robots = []

    with open(INPUT_FILE, "r") as f:
        for line in f.readlines():
            d = {}
            p, v = line.split()
            d["p"] = list(map(int, p[2:].split(",")))
            d["v"] = list(map(int, v[2:].split(",")))
            robots.append(d)


    part1(robots)
    print(f"Part 2: {part2(robots)}")

if __name__ == '__main__':
    main()