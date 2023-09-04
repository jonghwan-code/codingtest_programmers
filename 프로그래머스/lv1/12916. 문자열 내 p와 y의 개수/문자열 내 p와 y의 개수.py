def solution(s):
    # answer = True
    s = s.lower()
    p, y = (0, 0)
    # if 'p' in s or 'y' in s:
    for x in s:
        if x == 'p':
            p += 1
        elif x == 'y':
            y += 1
    if p == y:
        return True
    else:
        return False
    return True 