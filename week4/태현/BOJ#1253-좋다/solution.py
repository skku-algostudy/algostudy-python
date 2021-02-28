# BOJ#1253 - 좋다

# 어떤 수가 다른 수 두 개이 합으로 나타낼 수 있다면 그 수를 좋다라고 표현
# N개가 주어졌을 때 좋은수는?
# * 위치가 다르면 같아도 다른 수이다.

# 1 2 3 4 5 6 7 8 9 10
# 10 9 8 7 6 5 4 3 2 1
# 큰수대로 정렬한다음에
# 그 다음으로 큰 수 뺀 나머지가 리스트 안에 존재하는지 체크

# ex. 10이면 다음으로 커서를 옮겨 9를 10에서 빼고 그 나머지를 리스트 안에서 찾는다. 없다면 계속 반복한다.


num = int(input())
num_list = list(map(int, input()))

num_list.sort(reverse=True)

cursor = 0
while cursor != len(num_list):
