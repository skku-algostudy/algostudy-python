# BOJ#1015 - 수열 정렬

# 도대체 문제가 무슨소리인가...

# 3
# a[0] = 2, a[1] = 3, a[2] = 1

# p[0] = 1, p[1] = 2, p[2] = 0

# b[p[0]] = a[0], b[p[1]] = a[1], b[p[2]] = a[2]

# b[1] = 2, b[2] = 3, b[0] = 1
# 1 2 3


n = int(input())
A = list(map(int, input().split()))

P = []
sorted_A = sorted(A)  # 오름차순으로 정렬(작은수부터)

# print(sorted_A)

for i in A:  # 원래 A수열의 원소로 인덱스를 파악한다.
    P.append(sorted_A.index(i))
    sorted_A[sorted_A.index(i)] = -1  # 찾은것은 초기화

for i in range(len(P)):
    print(P[i], end=' ')
