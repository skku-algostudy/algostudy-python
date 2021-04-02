'''
*** input ***
n : 개수
computers : [[]]

*** output ***
네트워크 수

*** approach ***
각각의 v에 대해 탐색 수행
만약 새로운 네트워크가 나오면 answer += 1
기본 dfs에서 visited를 활용해서 방문 안했으면 ㄱ, 했으면 스킵.

*** 헤맸던점 ***
인덱스 0~n-1인지 1~n인지 다시금 확인
프로그래머스 디버깅 환경은 어디서 에러가 났는지 알 수 없다.
-> vscode에서 꼭 돌려보자.

'''
def dfs(graph, v, visited, n):
    visited[v] = True

    for adjacent_v in range(n):
        # print(v, adjacent_v)
        if graph[v][adjacent_v] == 1 and (not visited[adjacent_v]):
            dfs(graph, adjacent_v, visited, n)


def solution(n, computers):
    visited = [False] * (n)
    answer = 0

    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(computers, i, visited, n)
    
    return answer

print(solution(3, [[1,1,0],[1,1,0],[0,0,1]]))