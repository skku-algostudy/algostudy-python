# 틀렸던 풀이
# input
n = int(input())
dists = []
for i in range(n):
    dist = list(map(int, input().split()))
    dists.append(dist)

d = [[0 for _ in range(101)] for _ in range(101)]

start_val = dists[0][0]  # 시작 부분의 값
d[start_val][0] = 1
d[0][start_val] = 1

for i in range(n):
    for j in range(n):
        if d[i][j] == 1:
            val = dists[i][j]
            d[i+val][j] += d[i][j]
            d[i][j+val] += d[i][j]

print(d[n-1][n-1])

# ====================================================
# 🚨 최종 풀이
# input
n = int(input())
dists = []
for i in range(n):
    dist = list(map(int, input().split()))
    dists.append(dist)

d = [[0 for _ in range(n)] for _ in range(n)]


d[0][0] = 1

for i in range(n):
    for j in range(n):
        # 끝나는 부분 처리를 안해주면 원래의 value값이 0이라서
        # 값이 더해져버린다.
        if i == n-1 and j == n-1:
            break

        val = dists[i][j]

        if i+val < n:
            d[i+val][j] += d[i][j]
        if j+val < n:
            d[i][j+val] += d[i][j]

print(d[n-1][n-1])
