def solution(s):
    ref = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = ''
    tmp = ''
    for c in s:
        if c.isdigit():
            result += c
        else:
            tmp += c
            if tmp in ref:
                result += str(ref.index(tmp))
                tmp = ''
            else:
                continue
    return int(result) 
    