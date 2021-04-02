# 이걸 왜 다시 풀자고 적어놨을까

n = int(input())
a = list(map(int, input().split()))
left, right = 0, n-1
flag = 0
while left <= right:
    mid = (left + right) // 2
    if a[mid] == mid:
        print(mid)
        flag = 1
        break
    if a[mid] > mid:
        right = mid-1
    else:
        left = mid+1
if flag == 0:
    print(-1)
