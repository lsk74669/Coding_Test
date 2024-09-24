def solution(s):
    return ' '.join([word.capitalize() if word else word for word in s.split(' ')])