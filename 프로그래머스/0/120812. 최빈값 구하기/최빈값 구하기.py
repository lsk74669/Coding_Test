from collections import Counter

def solution(array):
    counter = Counter(array)
    most_common = counter.most_common(2)

    if len(most_common) == 1 or most_common[0][1] != most_common[1][1]:
        return most_common[0][0]
    else:
        return -1