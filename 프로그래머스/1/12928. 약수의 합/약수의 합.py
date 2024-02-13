def solution(n):
    LIMIT = int(n**0.5)
    divisors = set()
    for i in range(1, LIMIT + 1 ):
        if n % i == 0:
            divisors.update([i, n//i])
    answer = sum(divisors)
    return answer