def solution(numbers):
    base = 0
    for x in range(10):
        base += x
    return base - sum(numbers)