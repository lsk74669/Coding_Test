def solution(numbers):
    answer = [-1] * len(numbers)
    temp = []
    
    for idx, i in enumerate(numbers):
        while temp and numbers[temp[-1]] < i:
            top_idx = temp.pop()
            answer[top_idx] =  i
        temp.append(idx)
                
    return answer