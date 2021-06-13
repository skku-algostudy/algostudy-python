def solution(arr, cmds):
    answer = []
    for i1, i2, i in cmds:
        answer.append(sorted(arr[i1-1:i2])[i-1])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
