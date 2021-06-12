# 저 123을 2d리스트로 다루면 코드길이 개선 가능

sp1 = [1, 2, 3, 4, 5]
sp2 = [2, 1, 2, 3, 2, 4, 2, 5]
sp3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]


def solution(answers):
    n = len(answers)
    i1 = i2 = i3 = 0
    an1 = an2 = an3 = 0
    for i in range(n):
        a = answers[i]
        if a == sp1[i1]:
            an1 += 1
        if a == sp2[i2]:
            an2 += 1
        if a == sp3[i3]:
            an3 += 1
        i1 = 0 if i1 == 4 else i1+1
        i2 = 0 if i2 == 7 else i2+1
        i3 = 0 if i3 == 9 else i3+1

    max_score = max(an1, an2, an3)
    answers = []
    if an1 == max_score:
        answers.append(1)
    if an2 == max_score:
        answers.append(2)
    if an3 == max_score:
        answers.append(3)

    return answers


print(solution([1, 2, 3, 4, 5]))
