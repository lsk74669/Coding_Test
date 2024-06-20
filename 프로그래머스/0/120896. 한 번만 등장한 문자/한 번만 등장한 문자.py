from collections import Counter

def solution(s):
    count = Counter(s)
    
    unique_chars = [char for char, cnt in count.items() if cnt == 1]
    
    unique_chars.sort()
    
    return ''.join(unique_chars)