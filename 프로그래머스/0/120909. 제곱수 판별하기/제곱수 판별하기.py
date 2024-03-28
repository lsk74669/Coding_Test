def solution(n):
    root_n = n ** 0.5
    if root_n.is_integer():
        return 1
    else:
        return 2
