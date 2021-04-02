# --- 기존 문제 풀이
'''
skill : 선행 스킬 순서        CBD = 210   C: 2, B: 1, D: 0 나머지: -1
- 순서에 대한 가중치를 체크할 수 있는 변수 생성
- 가중치는 비효율적
- no, 필요없는스킬제외하고 스킬생성
'''


# def skillcheck(skill, skill_trees):
#     num = 0
#     for elements in skill_trees:
#         real_skill = ""
#         chk = True
#         # 1. 필요없는 스킬 제거.
#         for i in elements:
#             if i in skill:
#                 real_skill += i
#         print(real_skill)
#         # 2. skill과 비교.
#         for i in range(len(real_skill)):
#             if skill[i] != real_skill[i]:
#                 chk = False
#                 break
#         # 3. 선행스킬 만족하면 개수 증가.
#         if chk:
#             num += 1
#     return num


# def solution(skill, skill_trees):
#     answer = skillcheck(skill, skill_trees)
#     return answer

# ====================================================
# --- 새로운 풀이 (런타임 에러)
# 이 풀이는 어디가 잘못된건지 모르겠음..


# def solution(skill, skill_trees):
#     answer = 0

#     simple_skills = []

#     # 필요없는 알파벳 제거
#     for each_skill in skill_trees:
#         simple_skill = ""
#         for alphabet in each_skill:
#             if alphabet in skill:
#                 simple_skill += alphabet
#         simple_skills.append(simple_skill)
#     # print(simple_skills)

#     # skill 순서와 비교
#     for simple_skill in simple_skills:
#         if len(simple_skill) == len(skill):
#             if simple_skill[0] == skill[0]:
#                 answer += 1
#         else:
#             if simple_skill[0] == skill[0]:
#                 answer += 1

#     return answer

# ====================================================
# --- 위에 있는 풀이를 수정한 것
# --- 와 조금만 손보면 정답이었음..

def solution(skill, skill_trees):
    answer = 0

    simple_skills = []

    for each_skill in skill_trees:
        simple_skill = ""
        # 필요없는 알파벳 제거
        for alphabet in each_skill:
            if alphabet in skill:
                simple_skill += alphabet
        # 조건 체크
        if simple_skill == skill[0:len(simple_skill)]
        answer += 1

    return answer


# ====================================================
# --- 다른 사람의 풀이
# for ~ else, pop(0)(- 이거 같은 경우는 복잡도 O(n))

# def solution(skill, skill_trees):
#     answer = 0

#     for skills in skill_trees:
#         skill_list = list(skill)

#         for s in skills:
#             if s in skill:
#                 if s != skill_list.pop(0):
#                     break
#         else:
#             answer += 1

#     return answer
