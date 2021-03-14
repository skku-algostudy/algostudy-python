# 그냥 다익스트라로 풀면 될 것 같은데, 시간 초과 뜸
# > pypy3 사용하면 시간 초과 안뜨고 그냥 파이썬은 시간 초과
# 결과까지 힙으로 처리해서 시간을 줄여보려고 하긴 했는데
# 각각의 연산들에 대해 시간 복잡도 생각해서 리팩토링해보기 
import heapq

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):      # 백만
    a, b = map(int, input().split())
    graph[a].append(b)

table = [1e9] * (n+1)
table[x] = 0
q = [(0, x)]
answer = []
while q:
    dis, node = heapq.heappop(q)
    if dis > table[node]:
        continue
    if dis == k:
        heapq.heappush(answer, node)
    for i in graph[node]:
        next_dis = dis + 1
        if next_dis < table[i]:    # 이걸 dis+1이 아니라 dis로 잘못함
            table[i] = next_dis
            heapq.heappush(q, (table[i], i))

if answer:
    while answer:
        print(heapq.heappop(answer))
else:
    print(-1)