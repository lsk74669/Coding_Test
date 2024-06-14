def solution(array, n):
    diff_array = [(abs(x - n), x) for x in array]
    
    diff_array.sort()
    
    return diff_array[0][1]