def solution(cards1, cards2, goal):
    aN, bN = (0, 0)
    for word in goal:
        if word in cards1:
            aI = cards1.index(word)
            if aI != aN:
                return 'No'
                break
            aN += 1
        if word in cards2:
            bI = cards2.index(word)
            if bI != bN:
                return 'No'
                break
            bN += 1
    else:
        return 'Yes'