def solution(arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        tmp = []
        for c, d in zip(a, b):
            tmp.append(c+d)
        answer.append(tmp)
    return answer
