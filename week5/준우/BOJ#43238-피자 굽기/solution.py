'''
input
7 3 : 오븐깊이 7에 피자반죽 3개가 들어감.
5 6 4 3 6 2 3 : 오븐의 지름 (위->아래)
3 2 5 : 피자반죽의 지름

output
2 : 위에서 두번째에 마지막 피자반죽이 들어감.

strategy
각각의 피자반죽마다 딱 걸리는 지점을 찾고 인덱스를 기억하기
반복하면 될듯?

'''

OVEN_DEPTH, PIZZA_N = map(int, input().split())
oven_lengths = list(map(int, input().split()))
pizzas = list(map(int, input().split()))

idx = OVEN_DEPTH

for pizza in pizzas:
    for i in range(idx):
        if pizza <= oven_lengths[i]:
            idx = i
            break

print(idx)