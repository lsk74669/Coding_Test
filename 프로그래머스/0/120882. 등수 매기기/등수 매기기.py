def solution(score):
    avg_scores = [(sum(s) / 2, i) for i, s in enumerate(score)]
    
    avg_scores.sort(reverse=True, key=lambda x: x[0])
    
    ranks = [0] * len(score)
    
    current_rank = 1
    for idx, (avg, original_index) in enumerate(avg_scores):
        if idx > 0 and avg == avg_scores[idx - 1][0]:
            ranks[original_index] = current_rank
        else:
            current_rank = idx + 1
            ranks[original_index] = current_rank

    return ranks
