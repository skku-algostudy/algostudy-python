import sys


testCase = int(sys.stdin.readline())
# dfs 탐색 함수


def dfs(node, cnt):
    check[node] = 1
    for n in graph[node]:
        if check[n] == 0:
            cnt = dfs(n, cnt+1)
    return cnt


for _ in range(testCase):
    # n: 나라 수, m: 비행기 종류
    N, M = map(int, sys.stdin.readline().split())

    # 그래프
    graph = [[] for _ in range(N+1)]

    # 그래프에 담아주는 데
    # 양방향이니까 다음과 같이
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    # 국가 방문했는지 체크하려고
    check = [0]*(N+1)

    # 처음 국가부터 출발
    check[1] = 0

    cnt = dfs(1, 0)

    print(cnt)
