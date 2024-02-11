def solution(num, n):
    remainder = num % n
    if remainder == 0:
        answer = 1
    else:
        answer = 0
    return answer 