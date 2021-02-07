n = int(input())
nums = sorted(list(map(int, input().split())))
answer = 0

for i in range(n):
    test_list = nums[:i] + nums[i+1:]
    l = 0; r = n-2
    while l<r:
        temp = test_list[l] + test_list[r]
        if temp == nums[i]:
            answer += 1
            break
        elif temp < nums[i]:
            l += 1
        else:
            r -= 1

print(answer)