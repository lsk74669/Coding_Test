def solution(myStr):
    stack = []
    answer = []
    
    for i in myStr:
        if i in ('a', 'b', 'c'):
            if len(stack) > 0:
                answer.append(''.join(stack))
                stack = []
        else:
            stack.append(i)
                
    if len(stack) > 0:
        answer.append(''.join(stack))
    else:
        if len(answer) == 0:
            answer = ['EMPTY']
    
    return answer