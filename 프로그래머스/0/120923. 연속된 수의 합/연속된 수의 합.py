def solution(num, total):
    avg = total // num
    start = avg - (num - 1) // 2
    return [start + i for i in range(num)]
