def solution(n):
    LIMIT = int(n ** 0.5)
    for i in range(1, LIMIT+1):
        if n / i == i:
            return (i+1)**2
    return -1