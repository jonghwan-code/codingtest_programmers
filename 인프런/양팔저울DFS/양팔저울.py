def DFS(L, sum):
    global res
    if L == n:
        if 0 < sum <= total:
            res.append(sum)
    else:
        DFS(L+1, sum + k[L])
        DFS(L+1, sum - k[L])
        DFS(L+1, sum)


if __name__ == '__main__':
    n = int(input())
    k = list(map(int, input().split()))
    total = sum(k)
    res = []
    DFS(0, 0)
    res = set(res)
    print(total - len(res))
