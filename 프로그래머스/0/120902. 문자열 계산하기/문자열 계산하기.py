def solution(my_string):
    my_list = my_string.split()
    answer = int(my_list[0])
    
    for idx, i in enumerate(my_list):
        if idx % 2 !=0:
            if i == '+':
                answer += int(my_list[idx+1])
            else:
                answer -= int(my_list[idx+1])
            
    return answer