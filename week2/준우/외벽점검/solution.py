'''
*** input ***
n : 외벽 수
weak : 약한 외벽 정보
dist : 친구가 갈 수 있는 

*** output ***
써야 할 친구 최솟값

*** 신경쓸 조건 ***
한번 출발하면 방향 못바꿈.
원형 : 끝점까지 가도 처음으로 되돌아오는거랑 또이또이 -> 2배를 늘리는 아이디어.
'''

from itertools import permutations # 순열은 permutations 조합은 combinations

def solution(n, weak, dist):
    weak_n = len(weak) # 약한 부분 찾고
    for i in range(weak_n): # 각 약한 벽에 대해
        weak.append(weak[i] + n) # 두 배로 늘려주는 아이디어.
    answer = 1e9 # 친구를 다 써도 모자랄 때로 초기화.

    for start in range(weak_n): # 인덱스는 시작점!! 두 배로 늘렸으므로 시작점은 1시 방향이 될수도 11시방향이 될수도 있다.
        friends_cases = list(permutations(dist, len(dist))) # 친구의 조합
        for friends in friends_cases: # 각 (순서의) 경우마다
            count = 1
            position = weak[start] + friends[count-1] # 일단 한 친구로 땜빵
            for index in range(start, start+weak_n): # 그러면 땜빵시작점 ~ 땜빵끝점까지
                if position < weak[index]: # 그 다음 친구로 땜빵해야 하면 땜빵
                    count += 1 # 역시 카운트를 늘리고
                    if count > len(dist): # 추가 땜빵이 불가능하면 종료.
                        break
                    position = weak[index] + friends[count-1] # position을 그 다음으로 이동하는 식.
            answer = min(answer, count)
    if answer > len(dist): # 이 경우는 처음과 같이 1e9인 경우밖에 없을 것.
        return -1
    return answer