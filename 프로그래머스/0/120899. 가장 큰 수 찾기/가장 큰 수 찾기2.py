def solution(array):
    dict = {}
    for idx, num in enumerate(array):
        dict[num] = idx
    array.sort()
    return array[-1], dict[array[-1]]
