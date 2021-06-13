def find_root(root_t, v):
    if root_t[v] != v:
        root_t[v] = find_root(root_t, root_t[v])
    return root_t[v]


def union_vs(parent_t, v1, v2):
    r1 = find_root(parent_t, v1)
    r2 = find_root(parent_t, v2)
    if r1 < r2:
        parent_t[r2] = r1
    else:
        parent_t[r1] = r2


def solution(vn, es):
    es.sort(key=lambda x: x[2])
    parent_t = [i for i in range(vn+1)]
    answer = 0
    for v1, v2, cost in es:
        if find_root(parent_t, v1) != find_root(parent_t, v2):
            answer += cost
            union_vs(parent_t, v1, v2)
    return answer
