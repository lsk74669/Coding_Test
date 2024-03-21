def solution(my_string, queries):
    my_string_list = [i for i in my_string]
    answer = my_string_list.copy()
    
    for s, e in queries:
        for i in range(0, e-s+1):
            my_string_list[s+i] = answer[e-i]
            
        answer = my_string_list.copy()
            
    return ''.join(my_string_list)