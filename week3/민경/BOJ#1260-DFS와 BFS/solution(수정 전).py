# 범용적인 규칙을 찾고 정리해서 코드로 옳길 것, 초기화 내용까지 포함될 수 있도록
# 직접적 구현이 아닌 방법적 구현 (둘 중 하나의 개념)

n, m, v = map(int, input().split())
table = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    table[a].append(b)
    table[b].append(a)
for i in range(1, n+1):
    table[i].sort()

def dfs(table, v, is_visited):
    for node in table[v]:
        if is_visited[node] != 1 and node != None:
            is_visited[node] = 1
            print(node, end=' ')
            dfs(table, node, is_visited)

is_visited = [0]*(n+1)
is_visited[v] = 1
print(v, end=' ')
print(dfs(table, v, is_visited))




