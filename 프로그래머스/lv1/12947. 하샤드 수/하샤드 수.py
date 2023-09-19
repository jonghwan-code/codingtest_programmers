def solution(x):
    tmpSum = sum(list(map(int, (str(x)))))
    # if x % tmpSum:
    #     return False
    # else:
    #     return True
    return x % tmpSum == 0