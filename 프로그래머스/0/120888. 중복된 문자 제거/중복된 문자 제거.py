def solution(my_string):
    mydic = {}
    answer = ''
    
    for str in my_string:
        if str not in mydic:
            mydic[str] = 1
        else:
            mydic[str] += 1
    for i in mydic:
        answer += i
        

    return answer