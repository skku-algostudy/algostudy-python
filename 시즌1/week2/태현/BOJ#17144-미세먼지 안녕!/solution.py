# 미세먼지 안녕!
# 백준 #17144
# 시뮬레이션 문제

# 1. 상하좌우라는 한정된 조건 - 좌표로 생각해볼 수 있는 아이디어
# 서 동 북 남
# dx = (0, 0, -1, 1)
# dy = (-1, 1, 0, 0)

# 2. 함수로 작성해서 접근하는 아이디어

# 3. 배열에 반복문이용해서 원소를 만들어내는 기법

# 4. 시뮬레이션 문제는 차분하게 조건에 따라 작성하는 문제인데, 나는 왜 못풀었는가?
# -- 긴 코드 작성에 대한 거부감 : 조금 더 여러문제를 손으로 풀어보면서 거부감을 줄일 필요가 있음

# 5. 격자배열이 나오는 문제는 배열/인덱스를 충실히 활용하여 접근하면 된다는 생각

# 6. 코드 참고 - 출처: https://juhee-maeng.tistory.com/97
# -- 다시 작성할 필요가 있기 때문에 아래의 코드는 다시 나의 코드로 작성하겠습니다.

# if __name__ = '__main__': ?


def spread():
    for x in range(r):  # 행
        for y in range(c):  # 열
            if board[x][y] > 0:
                cnt = 0
                for i in range(4):  # 상하좌우로 퍼트리기 위해
                    nx, ny = x + dx[i], y + dy[i]
                    if not (0 <= nx < r and 0 <= ny < c):  # 벽의 범위를 벗어나면
                        continue
                    if board[x][y] < 5:  # 5보다 작다면
                        continue
                    if (nx, ny) == (air_cleaner[0], 0):
                        continue
                    if (nx, ny) == (air_cleaner[1], 0):
                        continue
                    cnt = cnt + 1
                    board2[nx][ny] = board2[nx][ny] + board[x][y]//5
                board2[x][y] = board2[x][y] + board2[x][y] - board[x][y]//5*cnt


def clean():
    # 윗부분 반시계방향
    for i in range(air_cleaner[0]-2, -1, -1):
        board2[i+1][0] = board2[i][0]

    for i in range(1, c):
        board2[0][i-1] = board2[0][i]

    for i in range(1, air_cleaner[0]+1):
        board2[i-1][-1] = board2[i][-1]

    for i in range(c-2, 0, -1):
        board2[air_cleaner[0]][i+1] = board2[air_cleaner[0]][i]

    board2[air_cleaner[0]][1] = 0

    # 아랫부분 시계방향
    for i in range(air_cleaner[1]+2, r):
        board2[i-1][0] = board2[i][0]

    for i in range(1, c):
        board2[-1][i-1] = board2[-1][i]

    for i in range(r-2, air_cleaner[1]-1, -1):
        board2[i+1][-1] = board2[i][-1]

    for i in range(c-2, 0, -1):
        board2[air_cleaner[1]][i+1] = board2[air_cleaner[1]][i]

    board2[air_cleaner[1]][1] = 0


if __name__ == '__main__':
    ## 행(r), 열(c), 시간(t)
    r, c, t = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(r)]

    # 공기 청정기 행 위치
    air_cleaner = []
    for i in range(r):
        if board[i][0] == -1:
            air_cleaner.append(i)

    # 서 동 북 남
    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)

    # 1번 시행
    board2 = [[0]*c for _ in range(r)]
    spread()
    clean()

    # t-1번 시행
    for time in range(t-1):
        board = board2.copy()
        board2 = [[0]*c for _ in range(r)]
        spread()
        clean()

    # 전체 총합 구하기
    sumv = 0
    for i in range(r):
        for j in range(c):
            if board2[i][j] > 0:
                sumv = sumv + board2[i][j]
    print(sumv)
