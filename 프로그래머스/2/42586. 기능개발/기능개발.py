def solution(progresses, speeds):
    import math
    answer = []
    days_left = [math.ceil((100 - prog) / speed) for prog, speed in zip(progresses, speeds)]
    
    curr = days_left[0]
    count = 1
    
    for i in range(1, len(days_left)):
        if days_left[i] <= curr:
            count += 1
        else:
            answer.append(count)
            curr = days_left[i]
            count = 1
    
    answer.append(count)
    
    return answer