def solution(x, n):
    answer = []
    answer.append(x)
    while len(answer) != n:
        answer.append(answer[-1] + x)
    
    return answer