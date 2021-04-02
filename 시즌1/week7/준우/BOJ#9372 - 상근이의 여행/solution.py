'''
summary
모든 v 방문, 최소한의 e 거쳐가기.

input
2 : 두 개의 테스트 케이스
3 3 : 3개의 국가, 3종류의 비행기
1 2 : 1-2 edge
2 3 : 2-3 edge
1 3 : 1-3 edge
5 4 : 5개의 국가, 4종류의 비행기
2 1 : ...
2 3
4 3
4 5

output
2 : TC1에 대해선, 두 번 타면 됨
4 : TC2에 대해선, 네 번 타면 됨.

strategy
MST 아닌가요?

'''


def find_parent(parent: list, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent: list, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def get_mst_cost(vn: int, es: list):
    parent = [0] * (vn+1)
    for i in range(1, vn+1):
        parent[i] = i

    cost = 0
    for e in es:
        a, b = e
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            cost += 1

    return cost


tc_n = int(input())
for _ in range(tc_n):
    vn, en = map(int, input().split())
    es = []
    for __ in range(en):
        es.append(tuple(map(int, input().split())))

    print(get_mst_cost(vn, es))
