def solution(N, A, B):
    cnt = 0
    
    while A != B:
        A = (A + 1) // 2
        B = (B + 1) // 2
        cnt += 1
    
    return cnt
