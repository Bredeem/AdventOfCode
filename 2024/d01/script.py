from collections import Counter
from aocd import get_data

def find_total_difference(list_a: list, list_b: list):
    list_a.sort()
    list_b.sort()

    res = 0

    for num_a, num_b in zip(list_a, list_b):
        diff = abs(num_a - num_b)
        res += diff

    print(f'Total difference: {res}')

def find_similarity_score(list_a: list, list_b: list):

    b_freqs = dict(Counter(list_b))

    sim_score = 0

    for num_a in list_a:
        try:
            freq = b_freqs[num_a]
            
            sim_score += (num_a * freq)

        except KeyError:
            pass

    print(f'Similarity score: {sim_score}')

def main():

    list_a = []
    list_b = []

    inp = get_data(day=1, year=2024)

    for line in inp.split("\n"):
        nums = line.split()
        list_a.append(int(nums[0]))
        list_b.append(int(nums[1]))

    find_total_difference(list_a, list_b)

    find_similarity_score(list_a, list_b)
   

if __name__ == '__main__':
    main()