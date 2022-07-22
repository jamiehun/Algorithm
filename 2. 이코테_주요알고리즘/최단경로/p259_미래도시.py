""" 제대로 못풀었음 """
import sys
import heapq

# N (회사의 개수), M (경로의 개수) 입력
n, m = map(int, input().split())

# Input 입력
input = sys.stdin.readline

# graph 생성
graph = [[] for _ in range(n+1)]

# distance (최소 거리) 입력
distance = [INF] * (n + 1)

# for 문으로 연결되어 있는 회사 별로 거리 입력
for i in range(n + 1):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 다익스트라 알고리즘 수행
def dijkstra(start):
    q = []
    heapq.push(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.pop()
        if distance[now] < dist:
            continue
        # 인접한 노드들의 연결에 대한 확인
        else:
            for i in len(graph[a]):
                cost = dist + graph[now][i]



    

