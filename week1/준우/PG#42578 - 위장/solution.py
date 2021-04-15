def solution(clothes):
    clothes_dict = {}
    answer = 1
    for each in clothes:
        _, kind = each
        if kind in clothes_dict:
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1

    for n in clothes_dict.values():
        answer *= n+1

    return answer - 1


print(solution([["yellowhat", "headgear"], [
      "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
