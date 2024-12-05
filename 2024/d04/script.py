LENGTH = 140

directions = [(-1,-1), (-1, 0), (-1, 1),
              (0,-1),           (0,1), 
              (1,-1),  (1,0),   (1,1)]

diagonals = [(-1,-1), (-1,1),
             (1,-1),  (1,1)]

def inside_check(i, j, direction, step=3):
    end_i = i + (step*direction[0])
    end_j = j + (step*direction[1])

    if end_i < 0 or end_i >= LENGTH or end_j < 0 or end_j >= LENGTH:
        return False
    return True


def find_XMAS(search_field, i, j):
    
    res = 0

    for d in directions:
        if not inside_check(i, j, d):
            continue
        
        cat = search_field[i + d[0]][j + d[1]] + search_field[i + 2*d[0]][j + 2*d[1]] + search_field[i + 3*d[0]][j + 3*d[1]]

        if cat == "MAS":
            res += 1
    
    return res


def find_X_MAS(search_field, i, j):

    for d in diagonals:
        if not inside_check(i, j, d, step=1):
            return False
    
    diag_a = search_field[i-1][j-1] + search_field[i][j] + search_field[i+1][j+1]
    diag_b = search_field[i+1][j-1] + search_field[i][j] + search_field[i-1][j+1]

    ans = ["MAS", "SAM"]

    if diag_a in ans and diag_b in ans:
        return True
    return False       
    

# Arr is 140 x 140
def iterate_search_field(search_field: list[list[str]]):

    total_XMAS = 0
    total_X_MAS = 0

    for i in range(LENGTH):
        for j in range(LENGTH):
            if search_field[i][j] == "X":
                total_XMAS += find_XMAS(search_field, i, j)
            elif search_field[i][j] == "A":
                if find_X_MAS(search_field, i, j):
                    total_X_MAS += 1

    print(f"Total XMAS: {total_XMAS}")
    print(f"Total X-MAS: {total_X_MAS}")
    



def main():
    
    input_f = 'input.txt'
    with open(input_f, 'r') as f:
        search_field = []
        for line in f.readlines():
            search_field.append([c for c in line.strip()])

    iterate_search_field(search_field)




if __name__ == '__main__':
    main()