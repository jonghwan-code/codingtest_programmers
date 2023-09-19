def solution(n, m):
    x, y = n, m
    while x:
        x, y = y % x, x
    return [y, n * m // y]