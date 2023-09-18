def solution(n, m):
    res = []
    def gcd(n, m):
        n, m = sorted([n, m])
        while n:
            m, n = n, m % n
        return m
    
    return [gcd(n, m), n * m // gcd(n, m)]