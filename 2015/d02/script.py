
INPUT_FILE = "input.txt"

def part1(li: list[str]):
    paper_len = 0
    ribbon_len = 0
    for dims in li:
        l, w, h = [int(dim) for dim in dims.split("x")]
        paper_len += 2*l*w + 2*w*h + 2*h*l + min([l*w, w*h, h*l])
        
        short_s = [l,w,h]
        short_s.remove(max([l,w,h]))
        ribbon_len += 2*short_s[0] + 2*short_s[1] + l*w*h
    print(f"Part 1: {paper_len}")
    print(f"Part 2: {ribbon_len}")
    


def part2(li: list[str]):
    pass

def main():
    
    with open(INPUT_FILE, "r") as f:
        input_list = [l.strip() for l in f.readlines()]

    part1(input_list)


if __name__ == '__main__':
    main()