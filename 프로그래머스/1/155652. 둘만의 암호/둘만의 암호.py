def solution(s, skip, index):
    answer = []
    skip_set = set(skip) 
    
    for char in s:
        current = char
        steps = 0
        
        while steps < index:
            current = chr(ord(current) + 1)
            if current > 'z':  
                current = 'a'
            if current not in skip_set: 
                steps += 1
        
        answer.append(current)
    
    return ''.join(answer)