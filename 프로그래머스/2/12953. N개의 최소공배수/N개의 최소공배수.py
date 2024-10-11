def GCD(A, B):
    while A>=1 and B>=1:
        if A<B:
            B = B%A
        else:
            A = A%B
    if A >= 1:
        return A
    return B

def LCM(A, B):
    return int(A / GCD(A, B)) * B

def solution(arr):
    for i in range(len(arr)-1):
        arr[i+1] = LCM(arr[i], arr[i+1])
    return arr[-1]