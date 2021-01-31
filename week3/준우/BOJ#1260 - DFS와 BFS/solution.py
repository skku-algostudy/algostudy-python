'''
*** input ***
4 5 1 -> 4개의 vertex, 5개의 edge, 1번부터 시작.
1 2 -> 1-2 edge
1 3 -> 1-3 edge
1 4 -> 1-4 edge
...


*** output ***
1 2 4 3 -> DFS Result
1 2 3 4 -> BFS Result

*** strategy ***
1. 시작점 방문
2. 인접점들에 대해서 방문 안했다면 처리

*** points ***
두 점 사이 여러 개의 간선 가능
양방향.

*** 풀면서 ***
인자는 세 개 꼬박꼬박 넣어주기 (재귀 사용하기 때문.)
스택을 써서 구현한 형태가 이게 맞는가?
그래프 표현 : 2차원배열 vs 연결리스트

*** 정리 잘 해놓은 ***
https://velog.io/@i-zro/%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%BD%94%ED%85%8C-%EB%8C%80%EB%B9%84-DFSBFS-%EB%B0%B1%EC%A4%80-1260%EB%B2%88-DFS%EC%99%80-BFS
'''

from collections import deque

def dfs(graph, v, visited): # 재귀 없이 구현한다면 -> 스택
    #### 1. 시작점 방문 ####
    visited[v] = True
    print(v, end=' ')

    #### 2. 인접점들에 대해 처리 ####
    for adjacent_v in range(1, vn+1):
        if graph[v][adjacent_v] == 1 and (not visited[adjacent_v]):
            dfs(graph, adjacent_v, visited)

# def dfs_stack(graph, v, visited):
#     #### 1. 시작점 방문 ####
#     stack = [v]
#     visited[v] = True
    
#     #### 2. 인접점들에 대해 처리 ####
#     while stack:
#         v = stack.pop()
#         print(v, end=' ')

#         for adjacent_v in graph[v]:
#             if not visited[adjacent_v]:
#                 stack.append(adjacent_v)
#                 visited[adjacent_v] = True



def bfs(graph, v, visited):
    #### 1. 시작점 방문 ####
    q = deque([v])
    visited[v] = True

    #### 2. 인접점들에 대해 처리 ####
    while q:
        v = q.popleft()
        print(v, end=' ')

        for adjacent_v in range(1, vn+1):
            if graph[v][adjacent_v] == 1 and not visited[adjacent_v]:
                q.append(adjacent_v)
                visited[adjacent_v] = True


vn, en, start_v = map(int, input().split())
graph = [[0]*(vn+1) for _ in range(vn+1)]
dfs_visited = [False]*(vn+1)
bfs_visited = [False]*(vn+1)

for _ in range(en):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1
    # 처음에 이렇게 했다가 문제 발생.
    # graph[v1].append(v2) 
    # graph[v2].append(v1)

dfs(graph, start_v, dfs_visited)
print()
bfs(graph, start_v, bfs_visited)