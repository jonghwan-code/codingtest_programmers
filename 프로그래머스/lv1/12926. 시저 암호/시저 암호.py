# def check(c, number):
#     if 97 <= ord(c) <= 122:
#         return chr((ord(c) - ord('a') + number) % 26 + ord('a'))
#     if 65 <= ord(c) <= 90:
#         return chr((ord(c) - ord('A') + number) % 26 + ord('A'))
def solution(s, n):
    res = ''
    for x in s:
        if x == ' ':
            res += ' '
        elif 97 <= ord(x) <= 122:
            res += chr((ord(x) - ord('a') + n) % 26 + ord('a'))
        else:
            res += chr((ord(x) - ord('A') + n) % 26 + ord('A'))
    return res