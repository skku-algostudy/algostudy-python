def solution(number: str, k: int) -> str:
    n = len(number)
    sorted_number = sorted(enumerate(list(number)), key=lambda x: x[1])
    new_number = ['']*n
    for i in range(n-k, n):
        idx, num = sorted_number[i]
        new_number[idx] = num
    return ''.join(new_number)


assert solution('1924', 2) == '94', 'tc1'
