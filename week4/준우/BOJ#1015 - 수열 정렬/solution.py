'''
*** input ***
3 -> 배열 크기 3
2 3 1 -> A=2, 3, 1

*** output ***
1 2 0

*** solution ***
문제 이해를 잘 하자.. 문제가 한번에 이해가 되지 않음.
p[0] : 0
p[1] : 0, 1
p[2] : 0, 1, 2
p[3] : 0, 1, 2, 3
(순서 뒤죽박죽일수도.)

a : 37215
b : 24103


수열 p를
길이가 n인 배열 a에 적용하면
길이가 n인 배열 b가 된다.
b[p[i]]가 된다.
b[p[i]] == 2
3
1

오름차순 + 

P[0]

무슨소리지??????
'''

n = int(input())
a = list(map(int, input().split()))
a_sorted = sorted(a) # 중복 생각!
for i in range(len(a)):
    idx = a_sorted.index(a[i])
    print(idx, end=' ')
    a_sorted[idx] = -1



# print(sorted(list(enumerate(map(int, input().split()))), key=lambda x:x[1]))



