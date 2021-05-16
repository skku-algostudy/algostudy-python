from collections import deque

BLANK = U = 0
WALL = R = 1
D = 2
L = 3
ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution(board: list):
    n = len(board)
    q = deque((0, 0))
    visit_t = [[False]*n for _ in range(n)]
    visit_t[0][0] = True

    while q:
        r, c = q.popleft()
        for d in ds:
            dr, dc = d
            newr, newc = r+dr, c+dc
            if 0 <= newr < n and 0 <= newc < n and not visit_t[newr][newc]:
                visit_t[newr][newc] = True
                q.append((newr, newc))
