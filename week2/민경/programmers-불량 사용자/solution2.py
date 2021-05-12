# 각각의 아이디와 대응될걸 생각해서 permutation으로 처리하고
# 마지막에 중복만 체크
# set은 붕족을 제거해주기도 하지만, 순서를 고려하지 않을 때도 쓰인다

from itertools import permutations

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
    result = []
    for candi in permutations(user_id, ban_len):
        count = 0
        for user, banned in zip(candi, banned_id):
            if compare(user, banned):
                count += 1

        if count == ban_len:
            if set(candi) not in result:
                result.append(set(candi))

    return len(result)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
