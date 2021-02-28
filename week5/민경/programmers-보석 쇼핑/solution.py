def solution(gems):
    g_len = len(gems)
    cnt = len(list(set(gems)))
    if cnt == 1:
        return [1, 1]
    start, end = 0, 1
    flag = 0

    while end < g_len:
        for i in range(end, g_len):
            if cnt == len(list(set(gems[start: i+1]))):
                end = i
                flag = 1
                break
            if gems[start] == gems[i]:
                start += 1
                end = start + 1
                break
        if flag == 1:
            break

    answer = [start+1, end+1]
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))