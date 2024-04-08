def solution(num_list):
    answer_1 = 0
    answer_2 = 0
    for idx, num in enumerate(num_list):
        if idx % 2 == 0:
            answer_2 += num
        else:
            answer_1 += num
    
    if answer_1 >= answer_2:
        answer = answer_1
    else:
        answer = answer_2
    
    return answer