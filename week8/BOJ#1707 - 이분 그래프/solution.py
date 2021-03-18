from sys import stdin
from itertools import permutations
input = stdin.readline


def find_parent(parent_t, v):
    if parent_t[v] != v:
        parent_t[v] = find_parent(parent_t, parent_t[v])
    return parent_t[v]


def union_parent(parent_t, v1, v2):
    v1 = find_parent(parent_t, v1)
    v2 = find_parent(parent_t, v2)
    if v1 < v2:
        parent_t[v2] = v1
    else:
        parent_t[v1] = v2


tc_n = int(input())
for _ in range(tc_n):
    vn, en = map(int, input().split())

    es = []
    for _ in range(en):
        edge = tuple(map(int, input().split()))
        es.append(edge)

    vs = [i for i in range(1, vn+1)]  # [1, 2, 3]
    for big_graph in permutations(vs, vn):  # 123 132 213 231 312 321
        big_graph = list(big_graph)
        for sep_idx in range(1, (vn//2)+1):
            parent_t1 = [0]+big_graph[:sep_idx]  # 1 1 2 2 3 3
            parent_t2 = [0]+big_graph[sep_idx:]  # 23 23 13 13 12 12
            for e in es:
                v1, v2 = e
                if v1 in parent_t1 and v2 in parent_t2:
                    union_parent(parent_t1, v1, v2)

                if v1 in parent_t2 and v2 in parent_t2:
                    union_parent(parent_t2, v1, v2)

            pv1 = parent_t1[0]
            pv2 = parent_t2[0]
            t1_is_broken = False
            t2_is_broken = False
            for v in parent_t1:
                if v != pv1:
                    t1_is_broken = True
                    break
            for v in parent_t2:
                if v != pv2:
                    t2_is_broken = True
                    break

            if t1_is_broken and t2_is_broken:
                print('YES')
            else:
                print('NO')
