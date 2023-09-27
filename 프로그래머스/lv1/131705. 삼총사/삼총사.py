def solution(number):
    cb = [0] * 3
    def DFS(L, S, res=[]):
        if L == 3:
            if sum(cb) == 0:
                res.append(1)
        else:
            for i in range(S, len(number)):
                cb[L] = number[i]
                DFS(L + 1, i + 1, res)
        return len(res)
    return DFS(0, 0)