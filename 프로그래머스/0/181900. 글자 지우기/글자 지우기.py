def solution(my_string, indices):
    answer = ''
    sorted_indices = sorted(indices)
    
    for j, i in enumerate(sorted_indices):
        my_string = my_string[:i-j] + my_string[i+1-j:]
    return my_string