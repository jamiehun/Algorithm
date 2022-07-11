""" for문을 중첩해서 하나씩 확인할려고 했으나 이렇게 될 경우 네방향 모두 확인 불가함 """
""" 추가로 BFS가 추구하는 연관된 것들을 들렀다가는 것을 제대로 하지 못함 """
""" 답안에 나온 대로 큐와 네방향으로 실행되는 코드에 대한 완벽한 숙지 필요! """

# BFS로 풀기
# 라이브러리 불러오기
from collections import deque

# n, m 자료 입력받기
n, m = map(int, input().split())

# deque 생성
queue = deque()

# 그래프 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 함수 생성
def bfs(graph):
    count = 0
    
    # a와 b가 n, m으로 갈때까지 조건문 반복
    for a in range(n):
        for b in range(m):
        if graph[a][b] == 1:
            a += 1
            b += 1
            count += 1
        
    return count

print(bfs(graph, 0, 0))
