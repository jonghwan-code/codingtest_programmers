def solution(price, money, count):
    total = sum([price * (x + 1) for x in range(count)])
    return 0 if money > total else total - money