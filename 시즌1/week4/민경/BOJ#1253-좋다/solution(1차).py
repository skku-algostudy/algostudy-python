n = int(input())
arr = list(map(int, input().split()))
arr.sort()
plus_idx = 0
for i in range(n):
    if arr[i] <= 0:
        plus_idx += 1
answer = 0

def only_plus(my_idx):
    global arr, answer, plus_idx
    for k in range(my_idx-1, plus_idx-1, -1):
        for l in range(plus_idx, k):
            if arr[my_idx] == arr[k] + arr[l]:
                answer += 1
                return True
    return False

def only_minus(my_idx):
    global arr, answer, plus_idx
    for k in range(my_idx + 1, plus_idx):
        for l in range(plus_idx-1, k, -1):
            if arr[my_idx] == arr[k] + arr[l]:
                answer += 1
                return True
    return False

def together(my_idx):
    global arr, answer, plus_idx
    if my_idx < plus_idx:
        front, end = my_idx-1, plus_idx
    else:
        front, end = plus_idx-1, my_idx+1
    for k in range(front, -1, -1):
        for l in range(end, n):
            if arr[my_idx] == arr[k] + arr[l]:
                answer += 1
                return True
    return False

if plus_idx == 0:
    for i in range(n):
        only_plus(i)
elif plus_idx == n:
    for i in range(n):
        only_minus(i)
else:
    for i in range(plus_idx):
        if not only_minus(i):
            together(i)
    for j in range(plus_idx, n):
        if not only_plus(j):
            together(j)

print(answer)

