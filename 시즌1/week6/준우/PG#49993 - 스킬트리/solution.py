'''
params & return
'CBD' 라는 스킬학습순서가
["BACDE", "CBADF", "AECB", "BDA"] 중 몇 개에 부합하는지
리턴하면 됨.

strategy
cbd와 bacde를 예로 들어보자.
c는 하나만 있어도 되고
b가 있다면 그 전에 c가 있어야 하고
d가 있다면 그 전에 c, b가 있어야 한다.

즉 역순으로 비교해서
d가 있다면 앞으로 있는 것들은 전부 있어야 하고
d가 없다면 패스
b가 있다면 앞으로 있는것들은 전부 있어야 하고
b가 없다면 패스
...

'''


def available(order, tree):
    skill_used = False
    skill_idx = len(tree)  # 최초의 인덱스는 가장 크게.
    for skill in reversed(order):  # d b c 순으로 갈때
        if skill in tree:  # 만약 d스킬이 들어있다면
            skill_used = True
            temp_idx = tree.index(skill)  # 그 인덱스가 기존 인덱스보다 크다면 말이 안되므로 0 리턴
            if temp_idx > skill_idx:
                return 0
            else:  # 그게 아니면 skill_idx 갱신
                skill_idx = temp_idx
        elif skill_used:
            return 0
    return 1


def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        answer += available(skill, skill_tree)
    return answer


print(solution('cbd', ['bacde', 'cbadf', 'aecb', 'bda']))
