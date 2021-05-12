# 초기 진입 조건을 잘못 이해하고 잡았다가 시간 낭비한 문제
# 일차선 다리, 1초에 1만큼 움직인다. > 두 트럭이 동시에 같이 출발할 수 없다!

def solution(b_len, weight, t_weight):
    sec = 1
    now = 0
    t_weight.reverse()
    q = []

    while True:
        if q and q[0][1] == 0:
            now -= q[0][0]
            q.pop(0)
        if t_weight and now + t_weight[-1] <= weight:
            now += t_weight[-1]
            q.append([t_weight.pop(), b_len])
        if len(t_weight) == 0 and len(q) == 1:
            sec += q[0][1]
            break
        for i in range(len(q)):
            q[i][1] -= 1
        sec += 1
    return sec


print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))