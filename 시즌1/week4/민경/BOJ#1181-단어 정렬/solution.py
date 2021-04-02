# 람다 사용하면 될 것 같은데

n = int(input())
words = []
for _ in range(n):
    words.append(input())
words = list(set(words))
words = sorted(words, key=lambda x: (len(x), x))
for i in range(len(words)):
    print(words[i])
