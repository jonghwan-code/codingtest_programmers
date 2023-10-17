def solution(k, score):
    lastSingersPt = []
    honorList = []
    for x in score:
        honorList.append(x)
        honorList.sort(reverse=True)
        # if len(honorList) > k:
        #     honorList = honorList[:k]
        print(honorList[:k][-1])
        lastSingersPt.append(honorList[:k][-1])

    #     lastSingersPt.append(honorList[-1])
    return lastSingersPt