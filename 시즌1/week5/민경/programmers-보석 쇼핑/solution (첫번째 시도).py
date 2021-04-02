# 앞뒤에서 이동하며 결과 도출
# 최단 거리는 보장되나 맨 앞의 결과가 보장되지 않는다

def solution(gems):
    dic = {}
    g_len = len(gems)
    start, end = 0, g_len - 1
    for g in gems:
        dic[g] = g_len  # 나올 수 없는 값인 리스트 길이로 초기화

    for i in range(round(g_len / 2)):
        front_g, rear_g = gems[i], gems[g_len-1-i]      # 앞뒤에서 한칸씩 이동해오며

        if dic[front_g] == g_len:   # 아직 나오지 않은 보석이라면
            dic[front_g] = i    # 나온 위치 저장
        else:   # 나온적이 있다면
            if dic[front_g] == start:   # 지금 front 인덱스인 gem이 맨 앞에 있는 것과 같다면
                start += 1      # 맨 앞을 뒤로 한칸
            if dic[front_g] == end:     # 맨 뒤와 같다면
                end -= 1        # 맨 뒤를 앞으로 한칸
        if i != (g_len-1-i):    # 이동하는 인덱스가 중간에서 만나지 않은 경우, 같으면 굳이 한번 더 rear를 볼 필요가 없으니까
            if dic[rear_g] == g_len:    # 아직 나오지 않은 보석이라면
                dic[rear_g] = i     # 나온 위치 저장
            else:
                if dic[rear_g] == start:
                    start += 1
                if dic[rear_g] == end:
                    end -= 1

    answer = [start+1, end]
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))