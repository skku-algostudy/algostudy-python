# 채점 중 나오다가 틀림
from collections import deque

n, m, v = map(int, input().split())
table = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    table[a].append(b)
    table[b].append(a)
for i in range(1, n+1):
    table[i].sort()

def dfs(table, v, is_visited):
    print(v, end=' ')
    is_visited[v] = 1
    for node in table[v]:
        if is_visited[node] != 1:
            dfs(table, node, is_visited)

def bfs(table, v):
    is_visited = [0] * (n + 1)
    q = deque()
    q.append(v)
    is_visited[v] = 1
    print(v, end=' ')
    while q:
        for node in table[v]:
            if is_visited[node] != 1:
                q.append(node)
                is_visited[node] = 1
                print(node, end=' ')
        v = q.popleft()

is_visited= [0]*(n+1)
dfs(table, v, is_visited)
print()
bfs(table, v)