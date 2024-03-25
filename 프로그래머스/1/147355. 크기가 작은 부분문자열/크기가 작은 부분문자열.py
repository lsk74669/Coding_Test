def solution(t, p):
    my_list = []
    answer = []
    
    for i in range(0, len(t) - len(p)+1):
        my_list.append(t[i:i+len(p)])
    for j in my_list:
        if int(j) <= int(p):
            answer.append(j)
    return len(answer)
