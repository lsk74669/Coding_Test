def GCD(a, b):
    while a >= 1 and b >= 1:
        if a < b:
            b = b % a
        else:
            a = a % b
    if a >= 1:
        return a
    else:
        return b
    
def LCM(a,b):
    return int(a/GCD(a,b)) * b
        
def solution(n, m):
    answer = [GCD(n,m), LCM(n,m)]
    return answer