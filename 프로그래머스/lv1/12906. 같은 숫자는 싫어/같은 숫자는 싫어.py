def solution(arr):
    p = arr[0]
    res = [p]
    for i in range(1, len(arr)):
        if p != arr[i]:
            p = arr[i]
            res.append(p)
    return res
        
        
        
        
        