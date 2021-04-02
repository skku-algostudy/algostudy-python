'''
문제분석
N개의 수 중 '어떤 수'가 '다른 두 수 두개의 합'으로 나타낼 수 있다면 좋다.
N개의 수 중 위를 만족하는 수는 몇개인가?
중복 제거하지 않는다.


input
10 -> 10개 입력할 것이다.
1 2 ... 10 -> 10개수


output
좋은 수 개수



-> 음수일 수 있는 것을 간과함!

'''

from itertools import combinations


# def jota(num, nums): # num 아래에서만 놀면 되는거네?
#     for i in range(len(nums) - 1):
#         if nums[i] == num:
#             continue
#         for j in range(i+1, len(nums)):
#             if nums[j] != num and nums[i] + nums[j] == num:
#                 # print(f'{num} = {nums[i]} + {nums[j]}')
#                 return 1
#     return 0

n = int(input())
nums = sorted(list(map(int, input().split())))
answer = 0

if n not in (1,2):
    for i in range(2, len(nums)): # 3번째~끝까지
        for each in combinations(nums[:i], 2):
            # print(each[0], each[1], end=' / ')
            if each[0] + each[1] == nums[i]:
                answer += 1
                break
        # print()

print(answer)
    



# print(answer)