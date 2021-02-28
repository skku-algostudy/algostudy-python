# 럭키 스트레이트
# 점수를 반으로 나누어 왼쪽 합과 오른쪽 합이 같은지 체크하는 문제

# 1. 반으로 나눈다 -> 길이를 반으로 나눈다는 접근 -> len()//2 - 1 이 기준
# 2. 슬라이싱 해서 -> 좌우합을 구해주면 되겠다라는 아이디어

# 1차시도 runtime error
# len()함수안에 변수를 넣지 않은것
# int형으로 변환 x
# right_N에서 슬라이싱할때 끝부분을 -1한 것

N = list(map(int, input()))  # 123456 문자열로 저장
left_N = N[0:len(N)//2]
right_N = N[len(N)//2:len(N)]

print("LUCKY" if sum(left_N) == sum(right_N) else "READY")
