# 또 똑같이 푼거 같은데.. => 이름 안헷갈리게 똑바로 만들기
# 두번째 틀린건 이름 때문에 틀렸음
# eval 함수

from itertools import permutations
def operation(a, b, oper):
    if oper == '+':
        return a+b
    elif oper == '-':
        return a-b
    elif oper == '*':
        return a*b

def solution(expression):
    oper = {'+': 0, '-': 0, '*': 0}
    temp = ''
    exp = []
    for e in expression:
        if e in oper:
            oper[e] = 1
            exp.append(int(temp))
            exp.append(e)
            temp = ''
        else:
            temp += e
    exp.append(int(temp))
    used_oper = [x for x in oper.keys() if oper[x] == 1]

    answer = 0
    for rank in permutations(used_oper, len(used_oper)):
        exp2 = exp
        for r in rank:
            i = 1
            while len(exp2) > 1:
                if i > len(exp2) - 1:
                    break
                if exp2[i] == r:
                    calcul = operation(exp2[i-1], exp2[i+1], exp2[i])
                    if i + 1 == len(exp2) - 1:
                        exp2 = exp2[:i - 1] + [calcul]
                    else:
                        exp2 = exp2[:i - 1] + [calcul] + exp2[i+2:]
                else:
                    i += 1
        answer = max(abs(exp2[0]), answer)
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
print(solution("200-300-500-600*40+500+500"))




