# --- boj#1003 - 피보나치 함수
# --- 재귀함수를 이용해서 접근하려고 했을 때 시간 초과가 뜬다.
# --- 시간 문제를 해결하기 위해서는, dp로 접근해야만 하는 문제이다.
# --- 런타임 한 번 생겼었는데 dp 테이블의 범위가 맞지 않아 발생하는 문제였다.

n = int(input())
d = [[0 for _ in range(2)] for _ in range(41)]  # 40으로 만들었을때 런타임 에러 발생

d[0] = [1, 0]
d[1] = [0, 1]

nums = []
for _ in range(n):
    nums.append(int(input()))

for i in range(2, max(nums)+1):
    d[i][0] = d[i-1][0] + d[i-2][0]
    d[i][1] = d[i-1][1] + d[i-2][1]

for num in nums:
    print(d[num][0], d[num][1])
