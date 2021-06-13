'''
문제를 보자마다 heapq를 사용해야한다는 것을 떠올릴 수 있었다.. (발전..)
비슷한 문제가 있었는데

매순간 우선순위를 고려해야했었고,
배열을 매번 재정렬하면 효율성을 통과할 수 없기 때문에 heapq를 사용한다.
'''
import heapq


def check(arr, k):
    for a in arr:
        if a < k:
            return False
    else:
        return True


def solution(scoville, K):
    heap = scoville
    heapq.heapify(heap)
    cnt = 0

    while True:
        if check(heap, K):
            break
        cnt += 1
        scovile1 = heapq.heappop(heap)
        scovile2 = heapq.heappop(heap)
        newScovile = scovile1 + (scovile2 * 2)
        heapq.heappush(heap, newScovile)

        # 원소 1개일때 통과하는 경우를 고려안했었다.
        if len(heap) == 1 and not check(heap, K):
            return -1

    return cnt


print(solution([1, 2, 3, 9, 10, 12], 7))
