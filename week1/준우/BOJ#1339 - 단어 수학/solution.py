'''
input
2
AAA
AAA

output
1998
'''


words = []
n = int(input())

for _ in range(n):
    words.append(input())

word_priority = 0 # 해당 단어의 값
priorities = [0 for _ in range(26)] # 각 알파벳의 중요도

for word in words: # 각 단어마다
    exp = 0
    while word:
        word, alph = word[:-1], word[-1]
        priorities[ord(alph)-ord('A')] += 10**exp
        exp += 1

priorities.sort(reverse=True)

for i in range(9, 0, -1):
    word_priority += i * priorities[9-i]

print(word_priority)
