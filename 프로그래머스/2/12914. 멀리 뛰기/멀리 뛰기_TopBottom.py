def solution(n):
    dp = {1:1, 2:2}
    
    if n not in dp:
        dp[n] = solution(n-1) + solution(n-2)
    
    return dp[n] % 1234567
