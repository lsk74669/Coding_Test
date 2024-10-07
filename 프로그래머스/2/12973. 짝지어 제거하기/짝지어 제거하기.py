def solution(s):
    stack = []
    for word in s:
        if len(stack) == 0:
            stack.append(word)
        else:
            if stack[-1] == word:
                stack.pop()
            else:
                stack.append(word)
    if len(stack) == 0:
        return 1
    else:
        return 0

