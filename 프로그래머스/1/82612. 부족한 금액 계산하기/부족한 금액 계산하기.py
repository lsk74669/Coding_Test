def solution(price, money, count):
    total = price * (count * (count + 1)) // 2
    
    shortage = total - money
    
    return max(0, shortage)
