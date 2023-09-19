def solution(absolutes, signs):
    sum = 0
    for num, b in zip(absolutes, signs):
        if b:
            sum += num
        else:
            sum -= num
    return sum