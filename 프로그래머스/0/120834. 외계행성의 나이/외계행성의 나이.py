def solution(age):
    age_str = str(age)
    answer = ''
    for i in age_str:
        answer += chr(int(i)+ ord('a'))
    return answer