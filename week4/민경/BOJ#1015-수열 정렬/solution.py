# 효율성 생각 안하고 생각난대로 바로 푼 버전
# n 최대값이 작기 때문에 시간, 공간 복잡도 생각보다 적음
# 값, 기존 인덱스, 정렬 후 인덱스 모두 저장해서 상황에 맞는 요소 선택해서 정렬

n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    arr[i] = [arr[i], i]
arr.sort()
for i in range(n):
    arr[i].append(i)
arr = sorted(arr, key=lambda x: x[1])
for i in range(n):
    print(arr[i][2], end=' ')