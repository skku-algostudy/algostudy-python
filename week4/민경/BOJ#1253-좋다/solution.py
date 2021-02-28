# 투포인터, 배열 스플라이싱 사용
# 투포인터 문제 찾아 연습하고 유형에 익숙해지기
# 최대한 그 요소 주변에서 찾아야 한다고 생각했는데..

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0

for i in range(n):
    temp = arr[:i]+arr[i+1:]
    left, right = 0, n-2
    while left < right:
        compare = temp[left]+temp[right]
        if arr[i] == compare:
            answer += 1
            break
        elif arr[i] > compare:
            left += 1
        else:
            right -= 1

print(answer)