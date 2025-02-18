def solution(array):
    number = 0
    for element in array:
        number += str(element).count('7')
    return number
