def solution(n_str):
    n_list = []
    for idx, i in enumerate(n_str):
        if i != '0':
            n_str = n_str[idx:]
            break
    return n_str