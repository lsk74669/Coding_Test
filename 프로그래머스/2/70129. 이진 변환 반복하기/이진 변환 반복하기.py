def solution(s):
    cnt = 0
    total = 0

    while s != "1":
        removed = s.count('0')
        total += removed

        s = s.replace('0', '')
        s = bin(len(s))[2:]

        cnt += 1

    return [cnt, total]
