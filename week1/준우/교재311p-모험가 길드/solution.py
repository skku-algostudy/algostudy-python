# 공포도 X는 X명 이상.
# 오름차순 -> 쫩 쫘압 쫘아압 으로 했다가 지난번에 틀렸던 생각이 난다.

n = int(input())
people = list(map(int, input().split()))
people.sort() # 그리디의 키아이디어는 은근 정렬에서 많이 나오는듯.
group_n = 0
in_this_group = 0


for p in people:
    in_this_group += 1 # 그룹멤버 하나 일단! 추가한 다음에
    if in_this_group >= p: # 현재 사람의 공포도를 이겨낼 인원수라면
        group_n += 1 # 고대로 결성
        in_this_group = 0 # 그룹원 초기화

print(group_n)