# 직선 - 100
# 코너 - 500
# 최소비용
# 벽있으면 도로건설 X

# bfs + 경로 최소비용, 아직 잘 모르겠다.

import sys
from collections import deque


def solution(board):

    def bfs(start):
        answer = sys.maxsize
        dic = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
        length = len(board)
        visited = [[sys.maxsize]*length for _ in range(length)]
        visited[0][0] = 0

        q = deque([start])
        while q:
            x, y, c, d = q.popleft()
            for i in range(4):
                nx = x + dic[i][0]
                ny = y + dic[i][1]

                # 범위 안에 있는지, 벽이랑 부딪히지 않는지
                if 0 <= nx < length and 0 <= ny < length and board[nx][ny] == 0:
                    # 진행방향 체크(방향 그대로면 직선100, 바뀌면 코너600)
                    nc = c + 100 if i == d else c + 600
                    # 값이 더작으면 교체
                    if nc < visited[nx][ny]:
                        visited[nx][ny] = nc
                        q.append([nx, ny, nc, i])

        return visited[-1][-1]

    return min([bfs((0, 0, 0, 1)), bfs((0, 0, 0, 2))])
