def solution(absolutes, signs):
    result = []
    for n in range(len(signs)):
        result.append(absolutes[n] * 1) if signs[n] else result.append(absolutes[n] * -1)
    return sum(result)