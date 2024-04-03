def solution(my_string):
    answer = [0] * 52
    for i in my_string:
        if 'A' <= i <= 'Z':
            answer[ord(i) - ord('A')] += 1
        else:
            answer[ord(i) - ord('a') + 26] += 1
    return answer