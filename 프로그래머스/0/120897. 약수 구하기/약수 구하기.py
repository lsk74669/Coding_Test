def solution(n):
    LIMIT = int(n**0.5)
    answer = []
    
    for i in range(1, LIMIT+1):
        if n % i == 0:
            answer.append(i)
            if i != n//i:
                answer.append(n//i)
    answer.sort()
    return answer