# 부등호 종류에 따라 기존에 저장되어 있던 위치의 앞 뒤에 삽입

k = int(input())
arr = list(input().split())

# 최대값
maxi = ['9']
left = 8
start = 0
last = arr[0]
for i in range(len(arr)):
    if last != arr[i]:
        start = i
    if arr[i] == '<':
        maxi.insert(start, str(left))
    else:
        maxi.append(str(left))
    left -= 1
    last = arr[i]

# 최소값
mini = ['0']
left = 1
start = 0
last = arr[0]
for i in range(len(arr)):
    if last != arr[i]:
        start = i
    if arr[i] == '<':
        mini.append(str(left))
    else:
        mini.insert(start, str(left))
    left += 1
    last = arr[i]

print(''.join(maxi))
print(''.join(mini))





