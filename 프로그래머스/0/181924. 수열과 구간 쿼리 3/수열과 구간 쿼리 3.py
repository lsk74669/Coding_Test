def solution(arr, queries):
    for i, j in queries:
        a, b = arr[i], arr[j]
        arr[i] = b
        arr[j] = a
    return arr