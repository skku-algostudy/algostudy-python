'''
****** 확실한 정리를 하고 들어가자 ******
초록주석보단 주황주석!


가장 대표적인 테스트케이스는 만족했으나
다른 예시에서 어긋나네요 ㅜㅜ.
시간이 상당히 많이 걸린 문제인데 다른 분들의 접근방식이 궁금합니다.

input 예시
7 8 1 : 7*8 사이즈의 방, 1초 후의 상황을 알고 싶다.
0 0 0 0 0 0 0 9 : 미세먼지 정보는 다음과 같다. -1은 공기청정기, 0은 청정지역, 나머지는 미세먼지
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0

output 예시
미세먼지 양 합
  * map 상태를 기록 안하고 그냥 증감만 기록하면 안되나? : 안된다. 그때그때 위치와 미세먼지 양에 따라 확산되는 먼지가 다르기 때문. room 정보는 항시 들고 있어야 한다.


points : 미세먼지 확산 후 공기청정기 작동
1. 확산
  * 한 번에 일어나야 함. 그.. 한 번 확산이 일어났다고 해서 다음 거에 영향을 주면 안됨.
    * 그러면 새로운 room_changed를 만들어서 거기에 미세먼지 증감을 반영한 후
    * 일괄 반영하면 되겠다.

2. 공기청정기 -> 디버깅을 잘하자
  * 반시계 : r == 0 OR r == 공기청정기위 or (c == 0 && r<공기청정기위) or (c == C-1 && r<공기청정기위). 방향 네 번 꺾이는동안 문제에서 나온 대로 침착하게 구현하면 오케이.
  * 시계 : r == R-1 OR r== 공기청정기아래 or (c == 0 && r>공기청정기아래) or (c == C-1 && r>공기청정기아래). 또한 마찬가지.

0. 2차원 지도
* 방향벡터
* 지도안에 있는 좌표인지 확인

'''

room = []
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]


def is_spreadable(r, c):
    global R, C
    # map 안에 있으면서, 공기청정기가 아닌 지역.
    if 0 <= r < R and 0 <= c < C and room[r][c] != -1:
        return True
    else:
        return False


def get_room_after_second():
    # global R, C, machine_r` -> 안 써도 될듯?!
    
    ##### STEP 1 : 확산 #####
    changes_in_room = [[0]*C for _ in range(R)] # 오.. 여기서 R C 로 했다가 실수함.
    for r in range(R):  # 모든 맵의 위치에 대해 검사
        for c in range(C):
            if room[r][c] > 0:  # 미세먼지가 있다면
                spreading_dust = room[r][c] // 5  # 얼마나 확산되는지 먼저 구해주고
                spread_count = 0
                for dr, dc in zip(drs, dcs):  # 각 4방향에 대해
                    newr = r+dr
                    newc = c+dc
                    if is_spreadable(newr, newc):  # 퍼짐가능한 범위에 있다면
                        spread_count += 1
                        changes_in_room[newr][newc] += spreading_dust  # 퍼짐 반영
                room[r][c] -= (spreading_dust * spread_count)

    # 모두 퍼졌다면 이제 변화한 값 계산
    
    for r in range(R):
        for c in range(C):
            room[r][c] += changes_in_room[r][c]
    # pretty_print('순환전', room)


    ##### STEP 2 : 순환 #####
    # 반시계 : r == 0 OR r == 공기청정기위 or (c == 0 && r<공기청정기위) or (c == C-1 && r<공기청정기위). 방향 네 번 꺾이는동안 문제에서 나온 대로 침착하게 구현하면 오케이.
    # 시계 : r == R-1 OR r== 공기청정기아래 or (c == 0 && r>공기청정기아래) or (c == C-1 && r>공기청정기아래). 또한 마찬가지.
    

    # 순서는 화살표 꼭지 ~ 화살표 시작점

    # 반시계1 : 왼쪽 
    for r in range(machine_r-1, 1, -1):
        room[r][0] = room[r-1][0]

    # pretty_print('1번순환', room)

    # 반시계2 : 위쪽 
    for c in range(C-1):
        room[0][c] = room[0][c+1]
    
    # pretty_print('2번순환', room)

    # 반시계3 : 오른쪽
    for r in range(machine_r):
        room[r][C-1] = room[r+1][C-1]

    # pretty_print('3번순환', room)

    # 반시계4 : 아래쪽
    for c in range(C-1, 1, -1):
        room[machine_r][c] = room[machine_r][c-1]

    room[machine_r][1] = 0
    # pretty_print('4번순환', room)

    # 시계 1 : 왼쪽
    for r in range(machine_r+2, R-1):
        room[r][0] = room[r+1][0]
    # pretty_print('1번순환', room)


    # 시계 2 : 아래쪽
    for c in range(C-1):
        room[R-1][c] = room[R-1][c+1]

    # pretty_print('2번순환', room)


    # 시계 3 : 오른쪽 (row R-1~machine_r+2, column C-1)
    for r in range(R-1, machine_r+1, -1):
        room[r][C-1] = room[r-1][C-1]
    # pretty_print('3번순환', room)



    # 시계 4 : 위쪽
    for c in range(C-1, 0, -1):
        room[machine_r+1][c] = room[machine_r+1][c-1]

    room[machine_r+1][1] = 0
    # pretty_print('4번순환', room)

def get_total_dust():
    # pretty_print('결과', room)
    answer = 0
    for row in room:
        answer += sum(row)
    return answer + 2

def pretty_print(msg, room): # 디버깅용 출력
    print(f'===={msg}====')
    for row in room:
        print(row)
    print()


R, C, T = map(int, input().split())

for r in range(R):
    row = list(map(int, input().split()))
    
    if row[0] == -1:
        machine_r = r

    room.append(row)

machine_r -= 1

for _ in range(T):
    get_room_after_second()
    pretty_print(_, room)

print(get_total_dust())