# 중복 제거가 관건
# 인덱스 묶음을 정렬된 문자열로 만들어서 중복 제거
# 1번 5번 테케 실패

from itertools import product

def compare(user, banned):
    b_len = len(banned)
    if len(user) != b_len:
        return False
    for i in range(b_len):
        if banned[i] == '*':
            continue
        if banned[i] != user[i]:
            return False
    return True

def solution(user_id, banned_id):
    ban_len = len(banned_id)
    banned_list = [[] for _ in range(ban_len)]

    # banned_id 별 리스트 만들기 - 아이디의 인덱스 저장
    for i in range(ban_len):
        for j in range(len(user_id)):
            if compare(user_id[j], banned_id[i]):
                banned_list[i].append(j)

    #print(banned_list)
    temp = banned_list[0]
    for i in range(1, ban_len):     # banned의 개수가 정해져 있지 않기 때문에 product를 누적시키기
        temp = list(product(temp, banned_list[i]))
        for i in range(len(temp)):
            temp[i] = list(temp[i])
            if type(temp[i][0]) == list:
                for t in temp[i][0]:
                    temp[i].append(t)
                temp[i] = temp[i][1:]
    #print(temp)

    result = []
    for t in temp:
        if len(set(t)) != ban_len:  # 내부 중복 제거
            continue
        candi = sorted(t)
        if candi not in result:
            result.append(candi)

    return len(result)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))