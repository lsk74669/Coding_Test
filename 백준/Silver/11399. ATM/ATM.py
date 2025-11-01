N = int(input())
A = list(map(int, input().split()))

for i in range(1, N):
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = key

S = [0] * (N+1)
for i in range(N):
    S[i+1] = S[i] + A[i]
print(sum(S))