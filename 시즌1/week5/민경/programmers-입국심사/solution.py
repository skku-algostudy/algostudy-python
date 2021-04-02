# 처음 생각했던 방법이 맞네
# 두가지 테스트케이스에서 시간 초과
# mid를 예외로 두지 않는 풀이는 시간 초과가 나지 않았음, 두 코드 비교 분석하기

def solution(n, times):
    start, end = times[0], times[-1] * n
    while True:
        mid = (start + end) // 2
        man_cnt, answer = 0, 0
        for t in times:
            each = mid // t
            man_cnt += each
            answer = each * t if each * t > answer else answer
        if man_cnt == n:
            return answer
        elif man_cnt > n:
            end = mid-1
        else:
            start = mid+1

# mid를 예외로 두지 않는 풀이
def solution2(n, times):
    left, right = 1, max(times) * n
    while left < right:
        mid = (left + right) // 2
        if sum([mid // x for x in times]) < n:
            left = mid + 1
        else:
            right = mid
    return left

print(solution(6, [7, 10]))
print(solution2(6, [7, 10]))