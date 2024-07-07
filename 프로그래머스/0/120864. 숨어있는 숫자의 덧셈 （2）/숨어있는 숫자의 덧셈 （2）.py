def solution(my_string):
    answer = 0
    current = ''
    
    for char in my_string:
        if char.isdigit():
            current += char
        else:
            if current:
                answer += int(current)
                current = ''
    
    if current:
        answer += int(current)
    
    return answer