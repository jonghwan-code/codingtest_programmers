def solution(n):
    a = []
    for x in str(n):
        a.append(x)
    a.sort(reverse=True)
    result = ''
    for y in a:
        result += y
    return int(result)