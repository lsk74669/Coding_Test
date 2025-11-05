def solution(s):
    N = len(s)
    stack = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            c = s[(j + i)%N]
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    break
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
        else:
            if not stack:
                cnt += 1
    return cnt
