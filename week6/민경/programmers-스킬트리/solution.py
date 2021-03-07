def solution(skill, skill_trees):
    answer = 0
    for item in skill_trees:
        flag = 0
        ski = list(skill)
        for i in item:
            if i in ski:
                if i == ski[0]:
                    ski.pop(0)
                else:
                    flag = 1
                    break
        if flag == 0:
            answer += 1
    return answer

print(solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"]))