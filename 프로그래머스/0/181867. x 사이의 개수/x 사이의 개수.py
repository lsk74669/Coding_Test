def solution(myString):
    stack = []
    answer = []

    for i in myString:
        if i == 'x':
            answer.append(len(stack))
            stack = []
        else:
            stack.append(i)
            
    if len(stack) == 0:
        answer.append(0)
    else:
        answer.append(len(stack))
            
    return answer