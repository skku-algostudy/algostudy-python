def dfs(r, c):
    if r <= -1 or r >= n or c <= -1 or c >= m:
        return False
    if graph[r][c] == 0:
        graph[r][c] = 1
        # 이 네가지가 쭉쭉 깊게 들어가 다 끝나야지만 트루 리턴
        dfs(r-1, c)
        dfs(r, c-1)
        dfs(r+1, c)
        dfs(r, c+1)
        return True
    return False


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            answer += 1

print(answer)