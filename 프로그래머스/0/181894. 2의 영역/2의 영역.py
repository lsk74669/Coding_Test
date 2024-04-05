def solution(arr):
    idx_list = []
    for idx, i in enumerate(arr):
        if i == 2:
            idx_list.append(idx)
    answer = []
    if len(idx_list) > 0:
        answer.extend(arr[idx_list[0]:idx_list[-1]+1])
    else:
        answer.append(-1)
    
    return answer