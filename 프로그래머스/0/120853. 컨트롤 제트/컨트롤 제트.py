def solution(s):
    s_list = s.split()
    result = 0
    for idx, i in enumerate(s_list):
        if i == 'Z':
            result -= int(s_list[idx-1])
        else:
            result += int(i)
        
    return result