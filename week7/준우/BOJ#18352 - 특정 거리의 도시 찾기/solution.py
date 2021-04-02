'''
summary
최단거리 K인 도시 존재하지 않으면 -1 출력

input
4 4 2 1 : v 4개, e 4개, 최단거리가 2인 v는?, v1부터 출발
1 2 : e 1->2
1 3 : e 1->3
2 3 : e 2->3
2 4 : e 2->4

output
4 : 최단거리가 2인 v는 4이다.


strategy
특정 v에서 출발해 다른 v들까지의 최단거리를 구하고
그 중 거리정보와 매칭되는 v를 출력하면 된다.
전형적인 다익스트라... 라고 하기엔!

모든 가중치가 1이므로 BFS가 훨신 효율적이다
다만 이 경우엔 depth를 기록해 놓아야 하는데
일단 구글링 결과 딕셔너리를 활용하는 방법이 있기에 이를 활용해본다.
(https://stackoverflow.com/questions/10258305/how-to-implement-a-breadth-first-search-to-a-certain-depth/59555331#59555331)
-> in연산자가 쓰이네? 시간복잡도 탈락 -> TF만 기록하던 방문테이블을 depth를 나타내도록 써먹자.
+ 존재X시 -1 출력에 유의.
'''

from sys import stdin
from collections import deque
input = stdin.readline

vn, en, given_dist, start_v = map(int, input().split())

graph = [[] for _ in range(vn+1)]
depth_t = [-1]*(vn+1)  # visit_t 를 확장해 depth_t를 만듦! depth -1인건 아직 방문하지 않은거.

for _ in range(en):
    from_v, to_v = map(int, input().split())
    graph[from_v].append(to_v)

# BFS 시작
q = deque([start_v])
depth_t[start_v] = 0

while q:
    v = q.popleft()
    if depth_t[v] == given_dist:  # 0 1 1 1 2 2 2 2 2 ... given_dist일때 탈출
        break
    for adj_v in graph[v]:
        if depth_t[adj_v] == -1:
            q.append(adj_v)
            depth_t[adj_v] = depth_t[v] + 1

v_exists = False
for v in range(1, vn+1):
    if depth_t[v] == given_dist:
        v_exists = True
        print(v)

if not v_exists:
    print(-1)
