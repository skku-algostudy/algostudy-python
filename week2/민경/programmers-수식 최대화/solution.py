# 로직 미리 정리하고 코드 짜기

from itertools import permutations

def solution(expression):
    operate = {'+': 0, '-': 0, '*': 0}
    split_exp = []
    temp = ''
    for e in expression:
        if e in operate:
            operate[e] = 1
            split_exp.append(int(temp))
            split_exp.append(e)
            temp = ''
        else:
            temp += e
    split_exp.append(int(temp))
    used_oper = [x for x in operate.keys() if operate[x] == 1]

    answer = 0
    for rank in permutations(used_oper, len(used_oper)):
        # print(rank)
        calcul = split_exp
        for r in rank:
            i = 1
            while len(calcul) != 1:
                if i >= len(calcul):
                    break
                if calcul[i] == r:
                    temp, a, b = 0, calcul[i-1], calcul[i+1]
                    if r == '+':
                        temp = a+b
                    elif r == '-':
                        temp = a-b
                    elif r == '*':
                        temp = a*b

                    if b == calcul[-1]:
                        calcul = calcul[:i-1] + [temp]
                        break
                    else:
                        calcul = calcul[:i-1] + [temp] + calcul[i+2:]
                else:
                    i+=1
            answer = max(abs(calcul[0]), answer)
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))