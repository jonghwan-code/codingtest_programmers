def solution(arr):
    res = []
    for i in range(len(arr)):
        if res[-1:] == [arr[i]]:
            continue
        res.append(arr[i])
    return res
        
        
        
        
        