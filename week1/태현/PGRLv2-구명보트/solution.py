# 우선적으로 5단계의 단계에 따라 러프하게 문제를 접근해보겠습니다 :)
# 1. 문제의 가장 핵심적인 포인트 한가지 뽑아보기
# - 1.1 그에 따라 신경써야하는 조건을 나열한다.
# 2. 그 포인트를 어떤 방식(조건/알고리즘)으로 해결할 수 있는가?
# 3. 플로우 생각해보기
# 4. 구현 방식 생각해보기 (수도 코드, 구현 아이디어 등)
# 5. 실제코드 작성

# 1. 문제 핵심
# 무게 제한이 있는 구명보트를 최대한 적게 사용하는 것

# 1.1 세부조건
# -- 최대 2명씩 탈 수 있음
# -- 무게 초과해서 탈 수 없음

# 2. 포인트
# 구명보트 한 번 운행할 때 최대한 많이 태워야하기 때문에
# 몸무게가 가벼운 사람들 먼저 순차적으로 태우면 되지 않을까?
# 한번에 2명이 최대이기 때문에 몸무게가 작은 순서대로 태우는게 맞는 것 같다.

# 🌱 생각해보니 최소 + 최대 몸무게를 가진 사람을 태우는게 맞는거 같다.
# 🌱 어차피 2명씩 짝지어서 태워야 하고

# 3. 플로우
# 1) people 리스트 몸무게 작은 순서대로 sorting
# 2) 턴마다 100kg될때까지 pop해주기 (보트에 태웠다고 생각) + 카운팅 + 새로운 배열에 추가
# 3) people 배열이 비어있을때까지 반복


# #1 solution - 잘못된 풀이
# def solution(people, limit):
#     # variables
#     personOnBoard = 0  # 탑승하고 있는 사람 수
#     move_count = 0
#     weight_sum = 0  # 구명 보트 제한 체크

#     # init
#     people.sort()  # 작은 몸무게부터 정렬

#     for i in range(len(people)):

#         if personOnBoard < 2 and weight_sum + people[i] <= limit:
#             personOnBoard += 1
#             weight_sum += people[i]

#         else:
#             move_count += 1
#             personOnBoard = 0
#             weight_sum = 0
#             weight_sum += people[i]

#     return move_count + 1

# #2 solution
# 처음에 포인트를 잘못 잡았어가지고 풀이가 산으로 갔었다.
def solution(people, limit):

    # variables
    l_cursor = 0
    r_cursor = len(people)-1
    move_count = 0

    # init
    people.sort()  # 작은 몸무게부터 정렬

    while(l_cursor <= r_cursor):

        # -- 중복되는 부분은 제거 good, 하지만 처음부터 효율적으로 짜려고 하기 보다는 일단 작성 후

        # 최소 + 최대 더했을때 초과된다면 r_cursor만 이동
        if people[r_cursor] + people[l_cursor] > limit:
            move_count += 1
            r_cursor -= 1

        # 최소 + 최대 더했을때 limit 이하라면 l_cursor, r_cursor 둘 다 이동
        else:
            move_count += 1
            l_cursor += 1
            r_cursor -= 1

    return move_count
