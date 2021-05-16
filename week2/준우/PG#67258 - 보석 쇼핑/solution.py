def solution(gems):
    n = len(gems)
    gem_dict = {}

    for gem in gems:
        if gem not in gem_dict:
            gem_dict[gem] = False
    total_gem_n = len(gem_dict)
    answer = [1, n]

    for start in range(n):
        count = 0  # count가 total_gem_n이 되는 순간 비교.

        for gem in gem_dict:  # gem_dict 초기화한후
            gem_dict[gem] = False

        for i in range(start, n):
            gem = gems[i]
            if not gem_dict[gem]:
                gem_dict[gem] = True
                count += 1
                if count == total_gem_n:
                    if answer[1] - answer[0] > i - start:
                        answer = [start+1, i+1]
                    break
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA",
                "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
