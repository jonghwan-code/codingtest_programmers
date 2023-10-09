def solution(cards1, cards2, goal):
    for word in goal:
        if len(cards1) > 0 and word == cards1[0]:
            cards1.pop(0)
        elif len(cards2) > 0 and word == cards2[0]:
            cards2.pop(0)
        else:
            return 'No'
            break
    else:
        return 'Yes'
            
        # if word in cards1:
        #     aI = cards1.index(word)
        #     if aI != aN:
        #         return 'No'
        #         break
        #     aN += 1
        # if word in cards2:
        #     bI = cards2.index(word)
        #     if bI != bN:
        #         return 'No'
        #         break
        #     bN += 1
    # else:
    #     return 'Yes'