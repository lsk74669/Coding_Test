from collections import Counter

def solution(strArr):
    answer = []
    for i in strArr:
        answer.append(len(i))
    
    
    return Counter(answer).most_common(1)[0][1]