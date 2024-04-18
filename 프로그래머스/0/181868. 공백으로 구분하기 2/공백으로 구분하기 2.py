def solution(my_string):
    stack = []
    answer = []
    
    for i in my_string:
        if i == ' ':
            if len(stack) > 0:
                answer.append(''.join(stack[:]))
            stack=[]
        else:
            stack.append(i)
            
    if len(stack) > 0:
        answer.append(''.join(stack[:]))
    return answer