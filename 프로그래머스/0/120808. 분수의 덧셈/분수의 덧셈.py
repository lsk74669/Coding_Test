def GCD(A, B):
    while A >= 1 and B >= 1:
        if A < B:
            B = B % A
        else:
            A = A % B
    if A >= 1:
        return A
    return B

def LCM(A,B):
    return int(A / GCD(A, B)) * B

def solution(numer1, denom1, numer2, denom2):
    denom = LCM(denom1, denom2)
    numer = numer1*denom/denom1 + numer2*denom/denom2
    gcd_of_nu_de = GCD(numer, denom)
    
    answer = [numer //gcd_of_nu_de ,denom//gcd_of_nu_de]
    
    return answer