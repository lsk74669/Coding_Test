def solution(left, right):
    answer = 0
    
    for n in range(left, right + 1):
        LIMIT = int(n**0.5)
        divisors = set()
        for i in range(1, LIMIT + 1):
            if n % i == 0:
                divisors.update([i, n//i])
                    
        if len(divisors) == 0:
            continue
        elif len(divisors) % 2 == 0:
            answer += n
        else:
            answer -= n
    return answer