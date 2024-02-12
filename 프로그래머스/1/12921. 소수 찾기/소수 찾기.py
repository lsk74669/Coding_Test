def isPrime(N):
    LIMIT = int(N**0.5)
    for i in range(2, LIMIT +1):
        if N % i == 0:
            return False
    return True

prime_list = []

def solution(n):
    for i in range(2, n+1):
        if isPrime(i):
            prime_list.append(i)
    answer = len(prime_list)
    return answer