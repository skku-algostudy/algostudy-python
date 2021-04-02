'''
input
26

output
3

strategy
5, 3, 2로 나누어떨어지게 하거나 1을 빼는연산을 취할 수 있음.
그 중 최솟값을 구해야 하는거.

'''

n = int(input())
d = [0]*30001  # d[i]는 i를 input으로 넣었을 때의 최소연산수임.

for i in range(2, n+1):  # 2부터 n까지
    d[i] = d[i-1]+1  # 언제든 적용될 수 있는 옵션인, 하나를 일단 줄이고(min값 비교용)
    if i % 2 == 0:  # 2로 나누어 떨어진다면 둘 중 택1. 아래도 같음.
        d[i] = min(d[i], d[i//2] + 1)
    elif i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    elif i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[n])
