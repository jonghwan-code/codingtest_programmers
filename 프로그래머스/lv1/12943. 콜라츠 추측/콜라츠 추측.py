def collatz(x, count):
    if count == 500:
        return -1
    if x == 1:
        return count
    if x % 2 == 1:
        return collatz(x * 3 + 1, count + 1)
    if x % 2 == 0:
        return collatz(x / 2, count + 1)

def solution(num):
    if num == 1:
        return 0
    else:
        return collatz(num, 0)