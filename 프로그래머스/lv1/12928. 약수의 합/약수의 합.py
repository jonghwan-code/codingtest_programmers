import math

def solution(n):
    sqrt = int(math.sqrt(n))
    arr = []
    for i in range(1, sqrt + 1):
        if n % i == 0:
            arr.append(i)
            if n // i != i:
                arr.append(n // i)
    
    return sum(arr) 