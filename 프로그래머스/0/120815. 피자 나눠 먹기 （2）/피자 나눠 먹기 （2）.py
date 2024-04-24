def solution(n):
    i = 1
    
    while not (6 * i / n).is_integer():
        i += 1
    return i