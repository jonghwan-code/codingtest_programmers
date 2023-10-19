def count(k, text):
    num = 0
    for char in text:
        minC = 2147000000
        flag = False
        for key in k:
            if char in key:
                minC = min(key.index(char)+1, minC)
                flag = True
        if not flag:
            num = -1
            break
        num += minC
    return num

def solution(keymap, targets):
    result = []
    for text in targets:
        result.append(count(keymap, text))
    return result