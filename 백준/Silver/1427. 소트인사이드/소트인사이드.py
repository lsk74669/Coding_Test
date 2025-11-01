A = list(map(int, input()))
n = len(A)

for i in range(n-1):
    max_idx = i
    for j in range(i+1, n):
        if A[j] > A[max_idx]:
            max_idx = j
    A[i], A[max_idx] = A[max_idx], A[i]

print(''.join(map(str,A)))