def solution(a, b):
    f_op = int(str(a) + str(b))
    l_op = int(str(b) + str(a))
    
    if f_op >= l_op:
        return f_op
    else:
        return l_op