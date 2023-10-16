def solution(lottos, win_nums):
    count = 0
    for num in win_nums:
        count += lottos.count(num)
    min = count
    max = count + lottos.count(0)
    if min <= 1:
        min = 1
    if max == 0:
        max = 1
    print(min, max)
    return [7 - max, 7 - min]