'''
** input **
2 : 부등호 두개 넣을거야
< > : 각각을 스페이스로 구분해 입력

** output **
897 : 8<9>7이 들어갈 수 있는 최댓값이다.
021 : 0<2>1이 들어갈 수 있는 최솟값이다.

** approach **
https://copy-driven-dev.tistory.com/entry/%EB%B0%B1%EC%A4%80Python2529Greedy-%EB%B6%80%EB%93%B1%ED%98%B8
참조함.
'''

from operator import lt, gt
from itertools import permutations

n = int(input())
tmp = input().split()
ops = []
result = []
for each in tmp: # 부등호 함수를 저장하는 리스트
    ops.append(lt if each=='<' else gt)


nums = [i for i in range(10)] # 0~9
for comb in permutations(nums, n+1): # 0~9를 요리조리 배치해서 n+1개의 모든 경우의 수를 뽑아내겠다
    # comb는 길이가 n+1만큼 되겠지.
    go = True
    for i in range(n): 
        if not ops[i](comb[i], comb[i+1]): # 모든 경우에 대해 검사.
            go = False
            break

    if go:
        result.append(comb)

print(''.join([str(i) for i in result[-1]])) # 제일 마지막에 있는 게 가장 큰 값이고
print(''.join([str(i) for i in result[0]])) # 제일 처음에 있는 게 가장 작은 값일 것이다.