def solution(num, k):
    num_str = str(num)
    k_str = str(k)
    
    try:
        index = num_str.index(k_str)
        return index + 1
    except ValueError:
        return -1