def solution(num_list):
    odd_list = []
    even_list = []

    for i in num_list:
        if i % 2 == 0:
            even_list.append(str(i))
        else:
            odd_list.append(str(i))
            
    even = ''.join(even_list)
    odd = ''.join(odd_list)
    return int(even)+int(odd)