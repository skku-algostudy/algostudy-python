'''
input
4 : 4바이4의 판
2 3 3 1 : 현재 칸에서 갈 수 있는 거리의 정보가 주어짐.
1 2 1 3
1 2 3 1
3 1 1 0

output
3 : 3가지 방법으로 점프해서 끝까지 갈 수 있음.

strategy
dp테이블을 어떻게 만들어야 할지 감도 잘 안온다.. 대충 2차원으로 만들어야 할 것 같긴 한데.
그래서 참조한 https://deok2kim.tistory.com/189
'''
N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
answer = 0

dp = [[0] * N for _ in range(N)]  # i,j까지 올 수 있는 경우의 수를 저장
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:  # 끝에 도달했을 때
            print(dp[i][j])
            break
        cur_cnt = field[i][j]
        # 오른쪽으로 가기
        if j + cur_cnt < N:
            dp[i][j + cur_cnt] += dp[i][j]
        # 아래로 가기
        if i + cur_cnt < N:
            dp[i + cur_cnt][j] += dp[i][j]
