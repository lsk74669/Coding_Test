def solution(array):
    sorted_array = sorted(array)
    
    answer = []
    answer.append(sorted_array[-1])
    answer.append(array.index(sorted_array[-1]))
    return answer