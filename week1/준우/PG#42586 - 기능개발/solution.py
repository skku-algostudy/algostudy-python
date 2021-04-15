from math import ceil


def solution(progresses, speeds):
    prev_day = ceil((100-progresses[0])/speeds[0])
    answer = [1]

    for p, s in list(zip(progresses, speeds))[1:]:
        day = ceil((100-p)/s)
        if day <= prev_day:  # 뒤의 작업이 먼저 혹은 같이끝난다면 앞에거와 같이 배포
            answer[-1] += 1
        else:  # 뒤에 작업이 더 걸린다면, 따로 배포
            answer.append(1)
            prev_day = day

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
