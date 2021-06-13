def solution(cs):
    n = len(cs)
    cs.sort()
    for i in range(n):
        if cs[i] >= n-i:
            return n-i
    return 0


print(solution([3, 0, 6, 1, 5]))
