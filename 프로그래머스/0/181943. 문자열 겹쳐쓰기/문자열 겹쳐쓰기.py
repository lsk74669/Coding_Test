def solution(my_string, overwrite_string, s):
    limit = len(my_string[:s]+overwrite_string)
    return my_string[:s] + overwrite_string + my_string[limit:]