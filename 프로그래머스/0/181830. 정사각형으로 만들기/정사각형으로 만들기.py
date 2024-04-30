def solution(arr):
    answer = arr.copy()
    print(answer[0])
    
    if len(answer[0]) > len(answer[1]):
        for i in range(len(answer[0])):
            answer[i].append(0)
    elif len(answer[0]) < len(answer[1]):
        for i in range(len(answer[1])):
            answer.append(0)
        
    return answer