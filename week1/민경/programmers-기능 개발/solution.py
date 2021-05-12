# 체크하는 포인트가 현재 개수에 포함되는지, 범위를 잘 체크하고 이후 로직을 짤 것
# 파이썬 zip 공부하기

import math

def solution(progresses, speeds):
    answer = []
    temp = []
    l = len(progresses)
    for i in range(l):
        temp.append(math.ceil((100-progresses[i]) / speeds[i]))
    time, idx = temp[0], 0
    for i in range(l):
        if time < temp[i]:
            answer.append(i-idx)
            time, idx = temp[i], i  # 지금 체크하고 있는 지점이 큰지를 확인하기 때문에, 해당 지점은 개수에 포함되지 않음, 따라서 다음 시작점이 i+1이 아닌 i가 된다.
        if i == l-1:
            answer.append(i-idx+1)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))