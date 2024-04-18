def solution(myString):
    stack = []
    answer = []
    
    for i in myString:
        if i == 'x':
            if len(stack) > 0:
                answer.append(''.join(stack))
                stack = []
        else:
            stack.append(i)
            
    if len(stack) > 0:
        answer.append(''.join(stack))
    return sorted(answer)