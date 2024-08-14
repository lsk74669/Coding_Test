def solution(n):
    new = ''
    while n > 0:
        n, remainder = divmod(n, 3)
        new = str(remainder) + new
    
    reversed = new[::-1]
    
    answer = int(reversed, 3)
    
    return answer