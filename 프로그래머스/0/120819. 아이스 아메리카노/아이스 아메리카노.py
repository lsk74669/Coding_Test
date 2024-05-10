def solution(money):
    num = money // 5500
    answer = [num, money - (5500 * num) ]
    return answer