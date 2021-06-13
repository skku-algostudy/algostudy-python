# R_W: red weight , B_W: brown weight
# R_H: red height , B_H: brown height

# R_W + 2 = B_W
# R_H + 2 = B_H
# B_H * B_W = brown
# R_H * R_W = red

# 가로길이 >= 세로길이
# red 부분을 탐색 (더 작은 크기이니까)
# brown = red+2


def get_brown_list(red):
    brown_list = []
    for i in range(1, int(red**0.5)+1):
        if red % i == 0:  # 약수의 짝을 구하는 과정
            # (왼=가로, 우=세로) : 가로가 세로길이보다 커야하므로 왼쪽에 큰값을 대입
            brown_list.append([red//i+2, i+2])  # brown은 red 보다 각각 2씩 크다
    return brown_list


def solution(brown, red):
    total_tile = brown + red  # 전체타일의 개수는 brown+red인데 이는 brown의 (너비)*(높이)와 같다
    brown_list = get_brown_list(red)
    print(brown_list)
    for tile in brown_list:
        if tile[0]*tile[1] == total_tile:  # tile[0]은 brown의 너비, tile[1]은 brown의 높이와 같다
            return tile

# 리스트를 만들어서 공간을 차지하는 것보다는 하나씩 체크하는게 더나음 - 준우


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
