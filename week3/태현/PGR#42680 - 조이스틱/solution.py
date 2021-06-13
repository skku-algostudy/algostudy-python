'''
매순간
- 위아래로의 선택
- 좌우로의 선택 (처음에만 선택하면 되지 않나 -> 좌우보고 A있으면 무조건 반대로 더한다.)
'''


def solution(name):

    answer = 0
    num_list = []
    idx = 0

    # 일단 최소값을 다 바꿔놓고 생각
    for ch in name:
        down = abs(ord('A') - ord(ch))
        up = abs(ord('Z') - ord(ch)) + 1
        num_list.append(min(down, up))

    # print(num_list)

    # 매순간 좌우에 대해 생각
    while True:
        answer += num_list[idx]
        num_list[idx] = 0

        if sum(num_list) == 0:
            break

        left, right = 1, 1

        while num_list[idx + right] == 0:
            right += 1

        while num_list[idx - left] == 0:
            left += 1

        if left >= right:
            idx += right
            answer += right
        else:
            idx -= left
            answer += left

    return answer


print(solution("JEROEN"))
print(solution("JAN"))
