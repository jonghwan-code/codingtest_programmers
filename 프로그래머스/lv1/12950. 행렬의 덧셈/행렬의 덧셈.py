def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr1[0])):
            num = arr1[i][j] + arr2[i][j]
            tmp.append(num)
        answer.append(tmp)
    return answer
