def solution(name, yearning, photo):
    my_dict = dict(zip(name, yearning))
    answer = []
    
    for i in photo:
        sum = 0
        
        for j in i:
            if j in my_dict.keys():
                sum += my_dict[j]
                
        answer.append(sum)
    return answer