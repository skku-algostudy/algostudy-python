from heapq import heappush as enqueue, heappop as dequeue
from sys import stdin

input = stdin.readline
INF = int(1e9)

vn, en = map(int, input().split())
graph = [[] for _ in range(vn+1)]
# parent_t = [0] * (vn+1)


for _ in range(en):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((v2, cost))
    graph[v2].append((v1, cost))

v1, v2 = map(int, input().split())


def dijkstra(from_v):
    q = []
    dist_t = [INF] * (vn+1)
    dist_t[from_v] = 0
    enqueue(q, (0, from_v))  # 그래프는 v, cost 순이지만 큐는 cost, v 순임에 유의
    while q:
        dist, v = dequeue(q)
        if dist_t[v] < dist:
            continue
        for adj in graph[v]:
            v_adj, dist_adj = adj
            cost = dist + dist_adj
            if cost < dist_t[v_adj]:
                dist_t[v_adj] = cost  # v와 v_adj를 헷갈리지 말것
                # parent_t[v_adj] = v
                enqueue(q, (cost, v_adj))  # v와 v_adj를 헷갈리지 말것
    return dist_t


# def print_path(to_v):
#     reversed_path = [to_v]
#     parent_v = parent_t[to_v]
#     while parent_v != 0:
#         reversed_path.append(parent_v)
#         parent_v = parent_t[parent_v]


t1 = dijkstra(1)
tv1 = dijkstra(v1)
tv2 = dijkstra(v2)

cost1 = t1[v1] + tv1[v2] + tv2[vn]
cost2 = t1[v2] + tv1[v2] + tv1[vn]

if cost1 >= INF and cost2 >= INF:
    print(-1)
else:
    print(min(cost1, cost2))
