'''
*** input ***
5 -> 그래프 5바이5
RRRBB -> RGB중 하나씩
GGBBB
BBBRR
BBRRR
RRRRR



*** output ***
4 3 -> 색약X는 4구역, 색약은 3구역으로 보임.


*** approach ***
적록색약 : R과 G를 같은 것으로 봄.
-> graph1, graph2로 나눠야겠다.
아까의 visited를 2차원으로 늘리면 될듯?

4방향 dfs 활용하면 되는데 어떻게 할지 감이 잡히지 않음.

*** review ***
list('merong') == ['m', 'e', 'r', 'o', 'n', 'g']


'''


def dfs(graph, v, visited, n):
    visited[n]

n = int(input())
graph1 = []
graph2 = []
for i in range(n):
    graph1.append(list(input()))