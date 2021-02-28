# 딕셔너리에서 아예 값을 뺌으로써 딕셔너리의 길이로 보석을 다 모았는지의 여부를 확인할 수 있도록
# 딕셔너리를 사용함으로써 시간 복잡도를 줄일 수 있도록

def solution(gems):
    include = {gems[0]: 1}
    g_len = len(gems)
    i_len = len(list(set(gems)))    # 보석 종류의 개수
    answer = [0, g_len-1]
    start, end = 0, 0       # 투 포인터

    while end < g_len and start < g_len:    # 두개의 포인터가 모두 범위 내에 있다면
        if len(include) == i_len:       # 보석 종류를 다 모았다면
            if (answer[1]-answer[0]) > (end-start): # 기존 값보다 새로운 값이 길이가 짧다면
                answer = [start, end]   # 새로운 값으로 갱신
            if include[gems[start]] == 1:   # 맨 앞을 다음 칸으로 이동
                del include[gems[start]]    # 한번 나왔으면 지우고
            else:
                include[gems[start]] -= 1   # 여러번 나왔으면 횟수에서 한번 빼고
            start += 1
        else:       # 보석 종류를 다 못 모았다면
            end += 1        # 뒤로 한칸 추가
            if end == g_len:    # 맨 뒤에 도달했다면
                break
            if gems[end] in include.keys(): # 이미 나온적이 있는 보석이라면
                include[gems[end]] += 1
            else:
                include[gems[end]] = 1

    answer = [answer[0]+1, answer[1]+1]
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))