def solution(num):
    def collatz(x, count):
        if count == 500:
            return -1
        elif x == 1:        
            return count
        else:
            if x % 2 == 1:
                return collatz(x * 3 + 1, count + 1)
            elif x % 2 == 0:
                return collatz(x / 2, count + 1)
    
    if num == 1:
        return 0
    else:
        return collatz(num, 0)