def solution(a, b, n):
    total = 0
    
    while n >= a:
        new = (n // a) * b
        total += new
        n = (n % a) + new
    
    return total
