def solution(seoul):
    answer = 0
    for idx, i in enumerate(seoul):
        if i == 'Kim':
            return f"김서방은 {idx}에 있다"
