# https://kdgt-programmer.tistory.com/60

# 걸릴 수 있는 시간이 될 수 있는 범위를 잡고, 이분탐색을 진행한다.
# 이분 탐색을 할 때에는, 그 대상을 항상 염두하자
# 이 문제의 경우, 답이 될 수 있는 검색 시간의 범위


def solution(n, times):
    answer = 0
    left, right = 1, n * max(times)

    while(left <= right):
        mid = (left + right) // 2
        temp = n
        for time in times:
            temp -= mid//time
            if temp <= 0:  # 심사대를 모두 이용하지 않았는데 모든 사람이 심사를 받는 경우 왼쪽으로 범위를 줄인다.
                answer = mid
                right = mid - 1
                break

        if temp > 0:  # 모든 심사대를 돌았는데 아직 사람이 남은 경우, 오른쪽으로 범위를 줄인다. (시간 +)
            left = mid + 1

    return answer
