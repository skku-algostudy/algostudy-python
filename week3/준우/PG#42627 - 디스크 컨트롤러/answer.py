# https://johnyejin.tistory.com/132
# 위 블로그 코드를 내 방식대로 재구성

def solution(jobs: list):
    answer = 0
    current_t = 0
    n = len(jobs)

    jobs.sort(key=lambda x: x[1])  # 소요시간 순으로 정렬

    while len(jobs) > 0:
        for i in range(len(jobs)):
            job = jobs[i]
            sijak, soyo = job
            if sijak <= current_t:  # 뭐 하나라도 작업할걸 발견한 경우
                current_t += soyo
                '''
                아 내가 라인코테에서 생각했던거는
                매 초마다, 그 때 들어와있는 모든 작업만큼 answer를 늘리려는 접근을 했었는데
                이걸 포함한 대부분의 풀이에선 그렇게 하지 않고, 각 작업별로 현시각-시작시각을 구해준 걸 더해줌으로서
                answer를 구해가고 있다.
                전형적인 구현문제인데, 답을 구해가는 방식에 대해서도 끊임없이 '이 방향이 효율적일까?' 하는 의문을 품고
                계속 생각해나가야겠다.
                '''
                answer += current_t - sijak
                jobs.pop(i)
                break
        else:  # break가 발생하지 않았을 때, 즉 작업할 작업이 없는 경우
            current_t += 1

    return answer // n


print(solution([[0, 3], [1, 9], [2, 6]]))
