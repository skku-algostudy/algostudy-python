'''
input
6 : 6명의 입국심사를 기다리는 사람이 있고
[7 10] : 심사관 한명은 심사시 7분, 한명은 10분이 걸린다

output
28 : 28분만에 6명의 심사가 끝남.

strategy
이진탐색을 적용한다면..
범위를 정해야 하는데
가장 오래 걸리는 경우는 젤 오래걸리는 사람이 싹 다 하는 경우겠지??
'''

def solution(n, times):
    start, end = 1, max(times)*n # 제일 오래 걸리는 경우를 end로 둠.
    while start <= end:
        mid = (start+end)//2
        # 그 후 무언가의 처리..?