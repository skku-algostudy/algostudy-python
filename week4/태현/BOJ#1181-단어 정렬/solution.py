# BOJ#1181 - 단어 정렬

# 알파벳 소문자로 이루어진 N개의 단어를 정렬하는 문제
# 1. 길이가 짧은순으로
# 2. 길이가 같으면 사전 순으로

# 2가지의 조건을 코드로 나타내면 된다.
# lambda 조건식을 이용하여 2가지 조건을 모두 커버하면 될 것 같다.

# 입력값
# 1. 들어올 단어의 개수 N개
# 2. N개의 단어들

# 중요한 조건 - 같은 단어가 들어오면 한번씩만 출력해야 한다.
# 단어랑 단어의 길이를 같이 저장하되, 중복 제거 처리 하면 좋을듯


num = int(input())
words = []

for i in range(num):
    word = input()
    words.append((word, len(word)))

# words라는 리스트에는 단어와 그 길이가 같이 튜플의 형태로 들어가 있음

words = list(set(words))  # 집합으로 중복 제거

words.sort(key=lambda word: (word[1], word[0]))  # 정렬

for word in words:
    print(word[0])
