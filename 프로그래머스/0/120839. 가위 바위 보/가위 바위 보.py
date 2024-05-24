def solution(rsp):
    my_dict = {'2': '0', '0': '5', '5': '2'}
    
    answer = []
    
    for char in rsp:
        answer.append(my_dict[char])
    
    return ''.join(answer)
