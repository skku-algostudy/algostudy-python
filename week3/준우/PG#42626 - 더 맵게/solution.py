from heapq import heappush, heappop, heapify


def solution(q, k):
    heapify(q)
    answer = 0
    while len(q) > 1:
        food1 = heappop(q)
        if food1 >= k:
            return answer

        food2 = heappop(q)
        heappush(q, food1 + 2*food2)
        answer += 1
    return answer if q[0] >= k else -1


print(solution([1, 2, 3, 9, 10, 12], 7))
