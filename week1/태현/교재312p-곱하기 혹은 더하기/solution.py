# 최대값을 만들기 위해서 곱하기 또는 더하기를 선택해야 하는데
# 0, 1이 피연산자인 경우에는 곱하기보다 더하기를 선택하는 것이 맞다.

nums = list(map(int, input()))

result = nums[0]
for i in range(1, len(nums)):

    if nums[i] <= 1 or result <= 1:
        result += nums[i]
    else:
        result *= nums[i]

print(result)
