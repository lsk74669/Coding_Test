def solution(code):
    ret= ''
    mode = 0
    for idx, i in enumerate(code):
        if i == '1':
            mode = 1-mode
        else:
            if mode == 0:
                if idx % 2 == 0:
                    ret += code[idx]
            else:
                if idx % 2 == 1:
                    ret += code[idx]
    if len(ret) == 0:
        ret = 'EMPTY'
    return ret