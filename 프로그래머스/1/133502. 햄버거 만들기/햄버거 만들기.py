def solution(ingredient):
    stack = []
    cnt = 0
    
    for item in ingredient:
        stack.append(item)
        
        if stack[-4:] == [1, 2, 3, 1]:
            del stack[-4:]
            cnt += 1
            
    return cnt
