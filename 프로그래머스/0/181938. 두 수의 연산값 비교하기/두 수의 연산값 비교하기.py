def solution(a, b):
    new_op = int(str(a)+str(b))
    old_op = 2 * a * b
    if new_op >= old_op:
        answer = new_op
    elif new_op < old_op:
        answer = old_op
    return answer