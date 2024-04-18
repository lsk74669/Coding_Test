def solution(myString, pat):
    stack = []
    m = len(pat)
    
    for i in myString:
        if i == 'A':
            stack.append('B')
            if ''.join(stack)[-m:] == pat:
                return 1
        else:
            stack.append('A')
            if ''.join(stack)[-m:] == pat:
                return 1
    
    return 0