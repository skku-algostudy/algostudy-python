'''
*** input ***
13 : 단어 13개
but : 13개의 단어 쭉 인풋받음
i
...
yours
...

*** output ***
13개 단어 정렬
1) 길이 짦은것부터
2) 길이 같으면 사전순으로


*** solution ***
구현 느낌이네.

빼먹은 조건 -> 같은 단어가 여러번 입력되는 경우 한 번만 출력!
'''

words = []
n = int(input())
for _ in range(n):
    words.append(input())

for word in sorted(list(set(words)), key=lambda x:(len(x), x)):
    print(word)