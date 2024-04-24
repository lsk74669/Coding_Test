def solution(arr, delete_list):
    delete_dict = {}
    answer = []
    
    for i in delete_list:
        delete_dict[i] = 0
        
    for idx,i in enumerate(arr):
        if i not in delete_dict:
           answer.append(i)
            
    return answer