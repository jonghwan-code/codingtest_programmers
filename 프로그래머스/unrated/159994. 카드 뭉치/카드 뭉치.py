def solution(cards1, cards2, goal):
    answer = ''
    for x in goal:
        if x != len(cards1) or x != cards2[0]:
            return 'NO'
            break
        elif x == cards1[0]:
            del cards1[0]
            print(cards1)
        else:
            del cards2[0]
            print(cards2)
    else:
        return 'YES'