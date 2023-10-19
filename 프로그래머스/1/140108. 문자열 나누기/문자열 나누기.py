def solution(s):
    result = 0
    while s:
        if len(s) == 1:
            result += 1
            s = ''
            break
        x = s[0]
        xC = 1
        not_xC = 0
        for i in range(1, len(s)):
            if x == s[i]:
                xC += 1
            if x != s[i]:
                not_xC += 1
            if xC == not_xC:
                result += 1
                s = s[i+1:]
                break
        else:
            result += 1
            break

    return result