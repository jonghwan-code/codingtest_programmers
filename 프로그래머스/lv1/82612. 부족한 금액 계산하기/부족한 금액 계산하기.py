def solution(price, money, count):
    total = sum([price * (x + 1) for x in range(count)])
    return max(0, total - money)
