from collections import deque

def DFS(node, graph, visited):
    if visited[node] == 1:
        return
    print(node, end=' ')
    visited[node] = 1
    temp = sorted(graph[node])
    for next in temp:
        DFS(next, graph, visited)


def BFS(node, graph):
    visited = [0] * (n+1)
    q = deque([node])
    while q:
        temp = deque.popleft(q)
        if visited[temp] == 1:
            continue
        visited[temp] = 1
        print(temp, end=' ')
        s = sorted(graph[temp])
        for next in s:
            if visited[next] == 0:
                q.append(next)

# 정점 개수, 간선 개수, 시작 위치
# 1000 by 1000이면 인접 행렬로도 되지 않을까
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # 인덱스 연산 없이 접근하기 위해
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
DFS(v, graph, visited)
print()
BFS(v, graph)