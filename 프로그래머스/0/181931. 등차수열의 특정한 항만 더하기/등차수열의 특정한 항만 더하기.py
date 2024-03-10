def solution(a, d, included):
    answer = 0

    for idx, j in enumerate(included):
        if j == True:
            answer += a+d*idx
    return answer