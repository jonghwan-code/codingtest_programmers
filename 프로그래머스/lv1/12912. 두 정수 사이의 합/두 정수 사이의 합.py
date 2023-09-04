def solution(a, b):
    tmp = [a, b]
    tmp.sort()
    x = (a + b) // 2
    y = (a + b) % 2
    if y == 1:
        return (tmp[1] - x) * (a + b)
    else:
        return x + ((tmp[1] - x) * (a + b))