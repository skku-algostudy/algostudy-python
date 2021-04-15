from collections import Counter


def solution(participants, completion):
    wanju_dict = Counter(participants)
    # wanju_dict = {}
    # for p in participants:
    #     if p in wanju_dict:
    #         wanju_dict[p] += 1
    #     else:
    #         wanju_dict[p] = 1
    for c in completion:
        wanju_dict[c] -= 1

    for each in wanju_dict:
        if wanju_dict[each] == 1:
            return each


print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],
               ["josipa", "filipa", "marina", "nikola"]))
