# 중간에 리스트로 만든 부분을 줄일 수 있지 않을까 싶은데
# 아이디어 자체가 어렵다기 보다 구조를 정리하는게 중요한 문제인 듯

def solution(genres, plays):
    ans = []
    temp = {}
    for idx, music in enumerate(plays):
        if genres[idx] in temp.keys():
            temp[genres[idx]].append((music, idx))
        else:
            temp[genres[idx]] = [(music, idx)]
    mid = []
    for gen in temp:
        mid.append([sum(x[0] for x in temp[gen]), gen])
    mid = sorted(mid, key= lambda x:x[0], reverse=True)
    for gen in mid:
        pick = sorted(temp[gen[1]], key=lambda x:x[0], reverse=True)
        ans.append(pick[0][1])
        if len(pick) > 1:
            ans.append(pick[1][1])
    return ans

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))