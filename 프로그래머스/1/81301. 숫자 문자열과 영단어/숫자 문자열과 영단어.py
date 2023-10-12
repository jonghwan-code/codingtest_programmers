from collections import deque
def solution(s):
    ref = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = ''
    stringChr = ''
    s = deque(s)
    while s:
        char = s.popleft()
        if char.isdigit():
            result += char
        else:
            stringChr += char
            if stringChr in ref:
                result += str(ref.index(stringChr))
                stringChr = ''
    return int(result) 