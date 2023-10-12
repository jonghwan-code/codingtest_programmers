def solution(s, n):
    res = ''
    for x in s:
        if x == ' ':
            res += x
        else:
            if 'A' <= x <= 'Z':
                tmp = 'A' 
            else:
                tmp = 'a'
            res += chr((ord(x) - ord(tmp) + n) % 26 + ord(tmp))
    return res