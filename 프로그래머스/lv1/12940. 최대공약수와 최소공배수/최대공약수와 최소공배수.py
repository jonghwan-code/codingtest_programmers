def solution(n, m):    
    def gcd(x, y):
        if x == 0:
            return y
        return gcd(y % x, x)
    
    return [gcd(n, m), n * m // gcd(n, m)]
            