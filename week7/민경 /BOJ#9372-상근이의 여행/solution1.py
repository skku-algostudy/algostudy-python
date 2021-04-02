# 이게 아마 말단 노드 반복적으로 솎아내 나가는 방식으로 접근한거
# 얘도 파이썬으로는 시간 초과 떴다

t = int(input())
for _ in range(t):
    # n이 국가수, m이 비행기 종류
    n, m = map(int, input().split())

    idx = [i for i in range(n+1)]
    table = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        table[a].append(b)
        table[b].append(a)

    cnt = 0
    while len(idx) > 1:
        flag = 0
        for i in idx:
            if len(table[i]) == 1:
                flag = 1
                cnt += 1
                table[table[i][0]].remove(i)
                idx.remove(i)
        if flag == 0:
            cnt += (len(idx[1:])-1)
            break
    print(cnt)