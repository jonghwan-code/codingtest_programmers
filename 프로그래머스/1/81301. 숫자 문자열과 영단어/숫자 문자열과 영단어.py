from collections import deque
def solution(s):
    ref = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = ''

    while s:
        for i in ref:
            if s.startswith(i):
              result += str(ref.index(i))
              s = s[len(i):]
              break
        else:
            result += s[0]
            s = s[1:]
            
    return int(result)