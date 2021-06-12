from itertools import permutations as cwr


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers: str) -> int:
    n = len(numbers)
    answer = 0
    num_dict = {}
    for pick_n in range(1, n+1):
        for each in cwr(numbers, pick_n):
            num = int(''.join(each))
            if num in num_dict:
                continue
            if is_prime(num):
                # print(num)
                answer += 1
            num_dict[num] = True

    return answer


print(solution("011"))
