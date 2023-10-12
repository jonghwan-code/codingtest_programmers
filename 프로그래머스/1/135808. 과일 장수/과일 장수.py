def solution(k, m, score):
    score.sort(reverse=True)
    def chunks(lst, n):
        for i in range(0, len(lst), n):
            if len(lst[i:i + n]) == n:
                yield lst[i:i + n]
    return sum([min(fruitsArr)*len(fruitsArr) for fruitsArr in list(chunks(score, m))])