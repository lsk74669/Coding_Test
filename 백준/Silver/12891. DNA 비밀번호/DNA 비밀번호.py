s, p = map(int, input().split())
A = input()
C = list(map(int, input().split()))

cnt = 0
current = [0, 0, 0, 0] 
check = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

for i in range(p):
    current[check[A[i]]] += 1

if all(current[i] >= C[i] for i in range(4)):
    cnt += 1

for i in range(p, s):
    current[check[A[i - p]]] -= 1  
    current[check[A[i]]] += 1      
    if all(current[j] >= C[j] for j in range(4)):
        cnt += 1

print(cnt)