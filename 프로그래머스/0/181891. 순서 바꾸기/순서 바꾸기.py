def solution(num_list, n):
    mylist = [0] * n
    for i in mylist:
        num_list.append(num_list[i])
        num_list.remove(num_list[i])
    return num_list