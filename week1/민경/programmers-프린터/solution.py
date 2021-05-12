def solution(priorities, location):
    answer = 0
    idx = [i for i in range(len(priorities))]
    while priorities:
        temp = priorities.pop(0)
        if priorities and temp < max(priorities):
            priorities.append(temp)
            idx.append(idx.pop(0))
        else:
            answer += 1
            temp = idx.pop(0)
            if temp == location:
                return answer
    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))