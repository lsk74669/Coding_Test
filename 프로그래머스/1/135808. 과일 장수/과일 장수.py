def solution(k, m, score):
    score.sort(reverse=True)
    
    answer = 0
    for i in range(0, len(score) - m + 1, m):
        min_score = score[i + m - 1]
        answer += min_score * m
    
    return answer