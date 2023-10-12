def solution(k, score):
    res = []
    honorList = []
    for x in score:
        honorList.append(x)
        if len(honorList) > k:
            honorList.remove(min(honorList))
        res.append(min(honorList))
    return res