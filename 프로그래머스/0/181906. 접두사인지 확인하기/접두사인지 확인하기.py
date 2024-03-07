def solution(my_string, is_prefix):
    answer = 0
    if len(my_string) > len(is_prefix):
        for i in range(len(is_prefix)-1):
            if my_string[i] == is_prefix[i]:
                answer = 1
            else:
                answer = 0
                break
    return answer