def solution(arr):
    mn = 1247000000
    for x in arr:
        if mn > x:
            mn = x
    result = list(filter(lambda x: x != mn, arr))
    return result if len(arr) > 1 else [-1]