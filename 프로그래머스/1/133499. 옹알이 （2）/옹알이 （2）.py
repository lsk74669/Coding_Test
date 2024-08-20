import re

def solution(babbling):
    cnt = 0
    words_list = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        if re.search(r'(aya|ye|woo|ma)\1+', word):
            continue
        
        temp = word
        for sound in words_list:
            temp = temp.replace(sound, ' ')
        
        if temp.strip() == '':
            cnt += 1
    
    return cnt
