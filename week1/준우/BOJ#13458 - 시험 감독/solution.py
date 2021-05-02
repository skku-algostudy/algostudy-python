from sys import stdin
input = stdin.readline

place_n = int(input())  # 시험장 수
examer_ns = list(map(int, input().split()))  # 응시자 수 리스트
chonggam, bugam = map(int, input().split())  # 총감 능력, 부감 능력
answer = place_n  # 총감수 깔고 시작

for examer_n in examer_ns:
    left_examer_n = examer_n - chonggam  # 총감이 감독 뛰고 남은 시험자수
    if left_examer_n <= 0:
        continue
    bugam_n = ((left_examer_n-1)//bugam)+1  # 부감 수 구해서
    answer += bugam_n  # 더해주기

print(answer)
