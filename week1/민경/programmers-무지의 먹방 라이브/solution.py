# 전에 풀었던 문제인데 정확도와 효율성을 높이고자 하였으나.. 실패해서 예전에 풀었던 코드를 올립니다

def solution(food, k):
    if sum(food) <= k:
        return -1

    L = len(food)
    m = k // L      # k번이 food를 돌 수 있는 최소 횟수 라고 생각

    # 최소 횟수에 따른 food 처리 (m바퀴를 이미 돌았다 가정)
    for i in range(L):
        if food[i] <= m:
            k -= food[i]
            food[i] = 0
        else:
            k -= m
            food[i] -= m

    j = 0       # j가 먹어야할 인덱스, 즉 답
    while k >= 0:       # k번 돈다
        if food[j] > 0:
            k -= 1
        j += 1
        j %= L

    if sum(food) <= 0:      # 다 돌았는데 다 먹었을 경우
        return -1

    return j

print(solution([3, 1, 2], 5))