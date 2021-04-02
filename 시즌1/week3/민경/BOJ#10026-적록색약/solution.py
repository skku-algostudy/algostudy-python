n = int(input())
pic = []

for _ in range(n):
    temp = input()
    pic.append(list(temp))

def dfs(row, col, color, is_visited):
    global pic
    if is_visited[row][col] == 1 or pic[row][col] != color:
        return
    is_visited[row][col] = 1
    vector = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for v in vector:
        new_row, new_col = row+v[0], col+v[1]
        if (0 <= new_row < n) and (0 <= new_col < n):
            dfs(new_row, new_col, color, is_visited)

def cycle(n, pic):
    answer = 0
    is_visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if is_visited[i][j] == 0:
                dfs(i, j, pic[i][j], is_visited)
                answer += 1
    print(answer, end=' ')

cycle(n, pic)
for i in range(n):
    for j in range(n):
        if pic[i][j] == 'G':
            pic[i][j] = 'R'
cycle(n, pic)



