# 딕셔너리로 만들어서 각 종류별로 리스트 길이 구하고 +1 해서(그 종류에서 선택하지 않을 경우) 곱한 다음에 1빼기 (아무것도 안입은 경우 제외)
# 접근은 맞았는데 또 파이썬의 쩌는 모듈이 있었군요.. from collections import Counter, from functools import reduce
# counter로 반복문 없이 각각에 대응되는 객체를 만들 수 있고, reduce로 또 반복문을 줄일 수 있네요
# 파이썬 모듈에 대해서도 공부하는게 좋을 것 같아요!

def solution(clothes):
    dic = {}
    answer = 1
    for c in clothes:
        if c[1] in dic.keys():
            dic[c[1]].append(c[0])
        else:
            dic[c[1]] = [c[0]]
    for key in dic.keys():
        answer *= (len(dic[key]) + 1)
    return answer - 1
