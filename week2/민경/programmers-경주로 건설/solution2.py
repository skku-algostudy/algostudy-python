from collections import deque

def solution(board):
    l = len(board)
    visited = [[1e9 for _ in range(l)] for _ in range(l)]
    go = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    q = deque([[0, 0, 0, -1]])
    while q:
        row, col, cost, direc = q.popleft()
        if visited[row][col] >= cost:
            visited[row][col] = cost
            for g in range(4):
                n_r, n_c = row + go[g][0], col + go[g][1]
                if 0 <= n_r < l and 0 <= n_c < l:
                    if board[n_r][n_c] == 0:
                        n_cost = cost + 100 if direc == -1 or direc == g else cost + 600
                        q.append([n_r, n_c, n_cost, g])
    return visited[l-1][l-1]

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
print(solution([
[0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
[0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
[0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
[1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 1, 0]]))