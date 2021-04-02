# 정렬 후에 반복문으로 k만큼 체크
# A의 값이 크거나 같을 경우 break, 정렬되어 있기 때문에 가능

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)
for i in range(k):
    if A[i] >= B[i]:
        break
    A[i] = B[i]
print(sum(A))