# 미완성

n, k = map(int, input().split())
table = []
where = [(0, 0, 0) for _ in range(k+1)]
for i in range(n):
    table.append(list(map(int, input().split())))
    for j in range(n):
        if table[i][j] != 0:
            virus = table[i][j]
            where[virus] = (virus, i, j)
s, x, y = map(int, input().split())

vector = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(s):
    length = len(where)
    for i in range(length):
        spot = where[i]
        for v in vector:
            row, col = spot[0]+v[0], spot[1]+v[1]
            if (0 <= row < n) and (0 <= col < n):
                if table[row][col] == 0:
                    print(row, col)
                    table[row][col] = spot[0]
                    #print(table)
                    where.append((spot[0], row, col))
print(table)
print(table[x-1][y-1])


