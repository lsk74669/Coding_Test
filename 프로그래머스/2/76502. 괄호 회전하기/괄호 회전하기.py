def solution(s):
    answer = 0
    n = len(s)
    for x in range(n):
        rotated_s = s[x:] + s[:x]
        if is_valid(rotated_s):
            answer += 1
    return answer

def is_valid(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack
