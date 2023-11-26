def solution(s):
    s = s.lower()
    p, y = (0, 0)
    for x in s:
        if x == 'p':
            p += 1
        elif x == 'y':
            y += 1
    # if p == y:
    #     return True
    # else:
    #     return False
    # return True 
    return p == y