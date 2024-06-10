def solution(n):
    def get_prime_factors(n):
        factors = []
        if n % 2 == 0:
            factors.append(2)
            while n % 2 == 0:
                n //= 2
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                factors.append(i)
                while n % i == 0:
                    n //= i
        if n > 2:
            factors.append(n)
        return factors
    
    return get_prime_factors(n)