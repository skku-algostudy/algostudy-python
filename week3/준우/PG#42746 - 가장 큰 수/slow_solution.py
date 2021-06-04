from itertools import permutations
INF = int(1e9)


def solution(ns):
    answer = -INF
    for perm in permutations(map(str, ns), len(ns)):
        answer = max(answer, int(''.join(perm)))
    return str(answer)


print(solution([6, 10, 2, 1, 5]))
