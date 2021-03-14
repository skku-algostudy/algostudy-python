from collections import deque

n, m, k, x = map(int, input().split())  # input()
node = [[] for _ in range(n+1)]

# 각각의 연결 관계를 표현해준다.
for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)

dist = [-1]*(n+1)
dist[x] = 0

q = deque([x])
print(q)

'''
-- 그래프 정보
  0 1 2 3 4
0 
1
2  o
3  o  o
4     o
'''

while q:
    now = q.popleft()
    # print(now)
    # print(node[now])

    for i in node[now]:
        # 미방문 노드라면 거리 증가 (각 거리가 1이기 때문에 +1)
        if dist[i] == -1:
            dist[i] = dist[now]+1
            # 새롭게 덱에 노드를 넣는 이유는 해당 노드에서 더 나아갈 수 있는 지를 체크
            q.append(i)
    # print(q)
# print(dist)

# k는 거리 정보
# k를 가지는 지점이 있는지 체크
for idx, d in enumerate(dist):
    if d == k:
        print(idx)
        break
else:
    print(-1)

# enumerate() 대신 사용 가능 - range()
# for i in range(1, vn+1):
#   if dist[i] == k:
#     print(i)
