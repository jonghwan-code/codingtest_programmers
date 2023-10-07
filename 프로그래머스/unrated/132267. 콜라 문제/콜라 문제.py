def solution(a, b, n):
    res = 0
    while n>=a:
        t, k = divmod(n, a)
        res = res + t*b
        n = (t*b)+k
    return res
                      
    # def answer(a, b, n, res):
    #     if n < a:
    #         return res
    #     else:
    #         t, k = divmod(n, a)
    #         res = res + t*b
    #         return answer(a, b, (t*b)+k, res)
    # return answer(a, b, n, 0)