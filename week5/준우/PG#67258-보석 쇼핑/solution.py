'''
input
['dia', 'ruby', 'ruby', 'dia', 'dia', 'emerald', 'sapphire', 'dia']
1번진열대엔 dia, 2번진열대엔 ruby, ..., 8번진열대엔 dia가 있음.

output
[3, 7]
3~7(r d d e s) 구매하는게 가장 짧은 구간으로 구매 가능.

strategy
이진탐색을 적용한다면...
처음이랑 끝을 잡고 점점 범위를 줄여나가는 형태가 될 것. in 연산자를 활용해야 하려나?
'''

def solution(gems):
    gem_n = len(set(gems))
    rang = [0, len(gems)-1]
    start = 0
    end = len(gems)-1
    while start <= end:
        ...