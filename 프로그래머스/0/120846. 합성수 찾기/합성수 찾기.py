def len_divisors(n):
    LIMIT = int(n ** 0.5)
    divisors = []
    
    for i in range(1, LIMIT + 1):
        if n % i == 0:
            divisors.append(i)
            if n//i != i:
                divisors.append(n//i)
    return len(divisors)
            

def solution(n):
    cnt = 0
    
    
    for i in range(2, n+1):
        if len_divisors(i) >= 3:
            cnt += 1

    return cnt