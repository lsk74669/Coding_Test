def solution(my_string):
    answer = ''
    
    for str in my_string:
        if ord(str) >= 97:
            answer += str.upper()
        else:
            answer += str.lower()
    return answer