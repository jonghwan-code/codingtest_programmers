import math
def solution(n):
    answer = False
    if int(math.sqrt(n)) == math.sqrt(n):
        answer=True
    else:
        answer = False
    if answer:
        return int(math.pow(math.sqrt(n) + 1, 2))
    else:
        return -1