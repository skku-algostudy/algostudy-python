# 한 번에 최대 두명이 아니라면?

def solution(people, limit):
    answer = len(people) # 원래 배는 사람수만큼 있는데, 같이 타면 하나씩 주는 느낌.
    
    people.sort(reverse=True) # 뚱뚱한 사람 먼저
    start_i = 0 
    end_i = len(people)-1
    
    while start_i < end_i:
        if people[start_i] + people[end_i] > limit: # 둘이 타면 배가 가라앉는다면? 뚱뚱 먼저
            start_i += 1
        else: # 다행히 둘이 탈 수 있는 경우라면, 
            start_i += 1
            end_i -= 1
            answer -= 1 # 배 하나 아끼기

    return answer