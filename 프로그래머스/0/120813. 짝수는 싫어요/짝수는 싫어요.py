def solution(n):
    answer = []

    i = 1
    while i <= n:
        answer += [i]
        i += 2
    return answer