def solution(x, n):
    result = [x]
    
    for i in range(1, n):
        result.append(result[i-1] + x)
    
    return result