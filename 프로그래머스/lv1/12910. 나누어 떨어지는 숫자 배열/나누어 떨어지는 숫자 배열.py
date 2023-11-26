def solution(arr, divisor):
    answer = sorted(list(filter(lambda x: x % divisor == 0, arr)))
    # return [-1] if len(answer) == 0 else answer
    return answer if answer else [-1]