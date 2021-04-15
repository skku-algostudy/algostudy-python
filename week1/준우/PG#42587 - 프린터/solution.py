from collections import deque


def solution(priorities, location):
    pr_asc = sorted(priorities)
    idx_pr_q = deque(enumerate(priorities))
    count = 0

    while idx_pr_q:
        if pr_asc[-1] == idx_pr_q[0][1]:
            count += 1
            if idx_pr_q.popleft()[0] == location:
                return count
            pr_asc.pop()
        else:
            idx_pr_q.append(idx_pr_q.popleft())

    return count


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
