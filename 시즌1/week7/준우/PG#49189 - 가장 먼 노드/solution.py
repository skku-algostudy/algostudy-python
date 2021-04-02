'''
summary
가장 멀리 떨어진 노드 개수 출력

params
vn=6
: 6개의 v
es=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
: 각 es

output
3 : 1번 노드에서 가장 멀리 떨어진 v는 3개

strategy
한 v에서 여러 v로
무방향, 가중치X
bfs로 depth 기록하면서 가장 멀리 떨어진 노드 보면 될듯!

'''

from collections import deque


def solution(vn, es):
    graph = [[] for _ in range(vn+1)]
    depth_t = [-1]*(vn+1)
    for e in es:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    q = deque([1])
    depth_t[1] = 0  # 1번 v의 depth는 0

    while q:
        v = q.popleft()
        for adj_v in graph[v]:
            if depth_t[adj_v] == -1:
                q.append(adj_v)
                depth_t[adj_v] = depth_t[v] + 1

    return depth_t.count(max(depth_t))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
