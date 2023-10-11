def solution(number):
    def compute_trio_count(students, selected):
        if len(selected) == 3:
            return 1 if sum(selected) == 0 else 0

        x = 0
        for i, score in enumerate(students):
            x += compute_trio_count(students[i + 1:], selected + [score])
        return x
    return compute_trio_count(number, [])