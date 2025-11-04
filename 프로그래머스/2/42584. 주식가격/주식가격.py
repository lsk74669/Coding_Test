def solution(prices):
    n = len(prices)
    answer = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if prices[i] > prices[j]:
                answer[i] = j-i
                break
            else:
                answer[i] = n-1-i
    return answer