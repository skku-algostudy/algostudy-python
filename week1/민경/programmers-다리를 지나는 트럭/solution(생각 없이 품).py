def solution(bridge_length, weight, truck_weights):
    answer = 1
    truck_weights.reverse()

    first = truck_weights.pop()
    temp = first
    q = [[first, bridge_length]]

    # 조건을 다르게 주고 천천히 생각하자
    while q:
        print(q)
        if truck_weights and temp + truck_weights[0] <= weight:
            temp += truck_weights[0]
            q.append([truck_weights.pop(), bridge_length])
        index = -1
        for i in range(len(q)):
            q[i][1] -= 1
            if q[i][1] == 0:
                index = i
                temp -= q[i][0]
        q = q[index+1:]
        answer += 1

    return answer

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100,[10,10,10,10,10,10,10,10,10,10]))