def solution(N, stages):
    from collections import Counter
    
    cnt = Counter(stages)
    
    total = len(stages)
    failure_rates = []
    
    for stage in range(1, N + 1):
        if total > 0:
            failed_users = cnt[stage]
            failure_rate = failed_users / total
            total -= failed_users
        else:
            failure_rate = 0
        
        failure_rates.append((stage, failure_rate))
    
    failure_rates.sort(key=lambda x: (-x[1], x[0]))
    
    return [stage for stage, rate in failure_rates]