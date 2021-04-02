# 가중치를 자릿수로 줘서 가중치 다 구한다음
# str을 int로 바꿔서 그에 맞춰 연산
# 문제를 무조건 쪼개지 말고 공통적으로 적용되는 규칙을 찾아보자

n = int(input())
words = []
for _ in range(n):
    words.append(input())

table = dict()
for word in words:
    for i in range(len(word)):
        if word[i] in table.keys():
            table[word[i]] += 10**(len(word)-1-i)
        else:
            table[word[i]] = 10**(len(word)-1-i)
temp = sorted(table.items(), key=lambda x: x[1], reverse=True)
match = [x[0] for x in temp]

sum = 0
for word in words:
    num = ''
    for i in range(len(word)):
        num += str(9-match.index(word[i]))
    sum += int(num)

print(sum)
