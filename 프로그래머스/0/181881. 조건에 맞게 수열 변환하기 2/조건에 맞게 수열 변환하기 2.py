def solution(arr):
    cnt = 0
    arr_1 = arr.copy()
    
    while True:
        arr_2 = arr_1.copy()
        
        for idx, i in enumerate(arr_1):
            if i % 2 == 0 and i >= 50: 
                arr_2[idx] = i // 2
            elif i % 2 == 1 and i < 50:
                arr_2[idx] = 2*i + 1
                
        if arr_1 == arr_2:
            break
        else:
            arr_1 = arr_2.copy()
            
        cnt += 1

    return cnt