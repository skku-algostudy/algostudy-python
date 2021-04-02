# 다익스트라로 구한 후 최대값의 인덱스를 취하면 될 것으로 보임
# 힙을 사용한 다익스트라의 시간 복잡도는 O(ElogV)

import heapq    # 힙은 항상 리스트 만들고 heapify나 heappush로 처리해주면 된다

def solution(n, edge):
    # 시작점은 1, 입력을 그래프화 해줘야
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    table = [1e9] * (n+1)
    table[1] = 0    # 이런 초기화와
    q = [(0, 1)]
    while q:
        dis, node = heapq.heappop(q)
        if table[node] < dis:   # 다른 최소 거리 노드를 거쳐온거 보다 이미 있는게 더 작다 > 이미 방문한 노드이다
            continue
        for adj in graph[node]:
            if table[adj] > dis+1:      # 이렇게 두 문장 모두를 조건 확인한 후 처리해서 중복 무한 발생하지 않도록, 논리적으로 생각해보기
                table[adj] = dis+1
                heapq.heappush(q, (table[adj], adj))
    answer = table.count(max(table[1:]))
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))