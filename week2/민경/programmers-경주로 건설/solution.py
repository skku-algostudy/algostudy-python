# 내가 원래 이런 식으로 중복으로 데이터 건드는건 항상 스택으로 했었는데 이번에 재귀로 도전해본건데
# 상황이 동시에 이루어지지 않기 때문에 중간에 막힐 수 있다는 문제가 있네
# 처음에 막혀있 수도 있잖아 바보야 을
# 최대한 통용되는 코드 짜기

def solution(board):
    l = len(board)
    visited = [[1e9 for _ in range(l)] for _ in range(l)]
    go = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우

    # 처음 코스트값은 0이 되어야 한다
    def find(row, col, cost, direc):
        if visited[row][col] >= cost:
            visited[row][col] = cost

            for g in range(4):
                n_r, n_c = row+go[g][0], col+go[g][1]
                if 0 <= n_r < l and 0 <= n_c < l:
                    if board[n_r][n_c] == 0:
                        n_cost = cost + 100 if g == direc else cost + 600
                        find(n_r, n_c, n_cost, g)

    right, down = 1e9, 1e9
    if board[0][1] == 0:
        find(0, 1, 100, 3)
        right = visited[l-1][l-1]
        visited = [[1e9 for _ in range(l)] for _ in range(l)]
    if board[1][0] == 0:
        find(1, 0, 100, 1)
        down = visited[l-1][l-1]

    return min(right, down)

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