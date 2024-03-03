def solution(my_string, is_suffix):
    answer = 0
    if len(my_string) >= len(is_suffix):
        for i in range(1, len(is_suffix)+1):
            if my_string[-i] == is_suffix[-i]:
                answer = 1
            else:
                answer = 0
                break
    return answer