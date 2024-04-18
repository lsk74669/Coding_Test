def solution(myString, pat):
    stack = []
    m = len(pat)
    result = 0
    
    for i in myString:
        stack.append(i)
        if ''.join(stack[-m:]) == pat:
            result += 1
            
    return result