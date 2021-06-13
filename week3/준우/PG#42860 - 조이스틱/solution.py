# 다른사람 풀이를 참조하자!

def solution(name):
    n = len(name)
    combo = False
    combo_n = 0
    max_combo_n = 0
    for a in name:
        if a == 'A':
            combo = True
            combo_n += 1
        elif combo:  # 콤보가 깨졌다면
            combo = False
            max_combo_n = max(combo_n, max_combo_n)
            combo_n = 0
    # l_combo = r_combo = 0
    # for i in range(1, n):  # 두번째부터 끝까지
    #     if name[i] != 'A':
    #         break
    #     r_combo += 1

    # for i in range(n-1, 0, -1):  # 마지막부터 두번째까지
    #     if name[i] != 'A':
    #         break
    #     l_combo += 1

    answer = n - 1 - max(l_combo, r_combo)
    for a in name:
        dist = abs(ord(a) - ord('A'))
        answer += min(dist, 26-dist)
    return answer


# BBAAAAAAAAAAAAAAAAABB -> 이런경우가 예외겠구나!
