from sys import stdin
from copy import deepcopy
input = stdin.readline
INF = int(1e9)


N = int(input())
jido = []
for _ in range(N):
    row = list(map(int, input().split()))
    jido.append(row)

shark_size = 2
eat_n = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
answer = 0
for r in range(N):
    for c in range(N):
        if jido[r][c] == 9:
            now_r = r
            now_c = c
            break

'''
먹을 수 있는 상황에선 이동할 거리 반환
없는 상황에선 -1 반환
'''


def get_dist():
    '''
    가까운 것부터 탐색하는 게 아닌 완전탐색이라, 시간복잡도에 문제가 생기지 않을까 우려되긴 함.(O(n^2))
    dist_jido엔 일반적인 경우 거리가 나오지만,
    먹을 수 없는 경우 -1로 하겠다.
    '''
    dist_jido = deepcopy(jido)
    for r in range(N):
        for c in range(N):
            if dist_jido[r][c] >= shark_size:  # 먹을 수 없거나 자기 자신인 경우 -1로 설정
                dist_jido[r][c] = INF
            else:
                dist = abs(now_r - r) + abs(now_c - c)
                dist_jido[r][c] = dist


while True:
    dist = get_dist()
    if dist < 0:
        break
    answer += dist

print(dist)
