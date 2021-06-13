# score: 50 - 70 - 100
''' 이야 스스로 풀어냈다... '''


def solution(n, lost, reserve):
    answer = 0

    # 반복문
    # - 도난당한 학생 체크하려고 배열 만듦
    arr = [0 for _ in range(n+2)]

    # - 도난당한 학생이 속해있는 인덱스는 1로 만들어주기
    # - 밑에 있는 조건문에서 사용하려고
    for i in lost:
        if i not in reserve:
            arr[i] = 1

    # 초기값
    # - 처음에는 체육활동할 수 있는 사람 수가
    # - (전체 학생 수 - 도난당한 학생 수)
    # - 나중에 빌려줄 수 있는 학생 늘어나면 +1 해주기
    answer = n - len(lost)

    for i in range(1, n+1):
        if i in reserve:
            # 여유있는데 본인이 도난당했을 때, 못빌려줘
            if i in lost:
                answer += 1
                continue
            # 내 왼쪽부터 체크할거야 무조건, 체크하고 빌려줄 수 있으면 빌려줘
            if arr[i-1] == 1:
                answer += 1
                arr[i-1] = 0
            # 최후, 왼쪽봤는데 빌려줄 필요없어 - 오른쪽 체크해 빌려줄 수 있으면 빌려줘
            elif arr[i+1] == 1:
                answer += 1
                arr[i+1] = 0

    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
