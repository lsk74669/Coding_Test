def solution(arr1, arr2):
    if len(arr1) != len(arr2):
        if len(arr1) > len(arr2):
            return 1
        else:
            return -1
    else:
        sum_arr1 = 0
        sum_arr2 = 0

        for i in arr1:
            sum_arr1 += i
        for j in arr2:
            sum_arr2 += j
        if sum_arr1 > sum_arr2:
            return 1
        elif sum_arr1 < sum_arr2:
            return -1
        else:
            return 0