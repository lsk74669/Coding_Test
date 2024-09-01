from collections import Counter

def solution(X, Y):
    cnt_x = Counter(X)
    cnt_y = Counter(Y)
    
    common = []
    
    for num in range(10):
        num_str = str(num)
        if num_str in cnt_x and num_str in cnt_y:
            common_count = min(cnt_x[num_str], cnt_y[num_str])
            common.extend([num_str] * common_count)
    
    if not common:
        return "-1"
    
    common.sort(reverse=True)
    answer = ''.join(common)
    
    if answer[0] == '0':
        return "0"
    
    return answer