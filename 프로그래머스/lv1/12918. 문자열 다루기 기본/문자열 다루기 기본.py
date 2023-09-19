def solution(s):
    # num = list(map(str, range(10)))
    if len(s) == 4 or len(s) == 6:
        # for x in s:
        #     if x not in num:
        #         return False
        #         break
        # else:
        #     return True
        return s.isdigit()
    else:
        return False