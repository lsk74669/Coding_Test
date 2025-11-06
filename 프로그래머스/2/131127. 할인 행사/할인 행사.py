def solution(want, number, discount):
    want_dic = {}
    cnt = 0
    for i in range(len(discount) - 5):
        for j in range(len(want)):
            want_dic[want[j]] = number[j]

        for d in discount[i:i+10]:
            if d in want_dic and want_dic[d] > 0:
                want_dic[d] -= 1
        if sum(want_dic.values()) == 0:
            cnt += 1
    return cnt
            
