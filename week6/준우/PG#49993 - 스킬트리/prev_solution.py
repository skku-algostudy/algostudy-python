'''
cbd라고 해보자.
뭐라도 있으면 let'sgetit 아예 없어도 가능함.
d를 찾고
    있으면 짤라서 진행 없으면 그대로 진행
b를 찾고
    있으면 짤라서 진행 없으면 그대로 진행
c를 찾고
    있으면 굳 없으면 빠꾸
'''


def is_ok(skill, tree):
    skill_used = False
    for each in skill:
        if each in tree:
            skill_used = True
            tree = tree[:tree.index(each)]
        else:
            if not skill_used:
                pass
            else:
                return 0
    return 1


def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        answer += is_ok(reversed(skill), tree)
    return answer
