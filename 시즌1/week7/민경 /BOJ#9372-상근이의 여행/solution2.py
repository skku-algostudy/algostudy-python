# 다익스트라, 말단 노드일 경우 거리 더한다
# 얘도 pypy로 하면 되는데 python은 시간 초과
import heapq

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    table = [1e9] * (n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    result = 0
    heap = [(0, 1)]
    while heap:
        dis, node = heapq.heappop(heap)
        if dis <= table[node]:
            if len(graph[node]) == 0:
                result += dis
            for next in graph[node]:
                if table[next] > dis+1:
                    table[next] = dis+1
                    heapq.heappush(heap, (dis+1, next))
    if result == 0:
        print(n-1)
    else:
        print(result)





