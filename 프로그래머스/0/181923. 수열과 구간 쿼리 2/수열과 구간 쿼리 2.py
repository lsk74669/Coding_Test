def solution(arr, queries):
    answer = []
    temp = []
    
    for s, e, k in queries:
        temp = []
        i_list = [i for i in range(s, e+1)]
        
        for i in i_list:
            if arr[i] > k:
                temp.append(arr[i])
        if len(temp)>0:
            answer.append(min(temp))
        else:
            answer.append(-1)
    return answer