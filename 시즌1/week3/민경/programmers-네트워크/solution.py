# 프로그래머스 - 네트워크
# 서로소 집합 문제로 볼 수 있음: 코드를 더 단순화할 수 없을까?

def find_parent(n, parent):
    if parent[n] == n:
        return n
    return find_parent(parent[n], parent)

def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def solution(n, computers):
    parent = [i for i in range(n)]
    for i in range(1, n):
        for j in range(0, i):
            if computers[i][j] == 1:
                union_parent(i, j, parent)

    for i in range(n):      # 루트 노드가 미반영된(나중에 추가된) 노드가 있을 수 있기 때문에
        parent[i] = find_parent(parent[i], parent)
    return len(list(set(parent)))

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))