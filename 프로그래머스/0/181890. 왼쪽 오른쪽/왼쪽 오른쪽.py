def solution(str_list):
    for idx, str in enumerate(str_list):
        if str == 'l':
            answer = str_list[:idx]
            break
        elif str == 'r':
            answer = str_list[idx+1:]
            break
        else:
            answer = []
    return answer