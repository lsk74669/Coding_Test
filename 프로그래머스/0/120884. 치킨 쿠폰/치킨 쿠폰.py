def solution(chicken):
    answer = 0
    coupon = chicken
    
    while coupon >= 10:
        service_chicken = coupon // 10
        answer += service_chicken
        coupon = service_chicken + (coupon % 10)
    
    return answer