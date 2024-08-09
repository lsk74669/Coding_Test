import itertools

def solution(number):
    count = 0
    for comb in itertools.combinations(number, 3):
        if sum(comb) == 0:
            count += 1
    return count
