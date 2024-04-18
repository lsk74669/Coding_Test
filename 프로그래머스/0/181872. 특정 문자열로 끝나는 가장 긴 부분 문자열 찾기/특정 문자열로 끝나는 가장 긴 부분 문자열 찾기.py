def solution(myString, pat):
    stack = []
    m = len(pat)
    
    for i in myString:
        stack.append(i)
        if ''.join(stack)[-m:] == pat:
            answer = ''.join(stack)
    
    return answer