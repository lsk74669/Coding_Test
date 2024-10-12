from collections import Counter

def solution(k, tangerine):
    cnt_size = Counter(tangerine)
    
    sorted_sizes = sorted(cnt_size.values(), reverse=True)
    
    cnt_type = 0
    selected_tangerines = 0
    
    for cnt in sorted_sizes:
        selected_tangerines += cnt
        cnt_type += 1
        if selected_tangerines >= k:
            break
    
    return cnt_type
