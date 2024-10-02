def solution(a, b):
    from math import gcd
    
    common_divisor = gcd(a, b)
    a_simplified = a // common_divisor
    b_simplified = b // common_divisor
    
    for prime in [2, 5]:
        while b_simplified % prime == 0:
            b_simplified //= prime
    
    if b_simplified == 1:
        return 1
    else:
        return 2
