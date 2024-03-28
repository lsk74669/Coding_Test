def solution(a, b, c, d):
    answer = 0
    
    score = [0] * 7
    for i in [a, b, c, d]:
        score[i] += 1

    p = score.index(max(score))
    mylist = [i for i,x in enumerate(score) if x == 1]

    if max(score) == 4:
        answer = 1111 * p
    elif max(score) == 3:
        q = score.index(1)
        answer = (10 * p + q)**2
    elif max(score) == 2 and len(mylist)==2:
        print(a)
        q,r = [i for i,x in enumerate(score) if x == 1]
        print(b)
        answer = q * r
    elif max(score) == 2:
        p, q = [i for i,x in enumerate(score) if x == 2]
        answer = (p+q) * abs(p-q) 
    else:
        answer = min(a, b, c, d)
    
    return answer