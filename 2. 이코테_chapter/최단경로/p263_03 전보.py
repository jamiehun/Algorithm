'''다익스트라 알고리즘을 좀 더 잘 이해해야함 (heapq구조)'''
'''다익스트라 알고리즘을 구현하는 코딩을 외울정도로 연습해야함'''

# 라이브러리 import
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

# 도시의 개수(n), 통로의 개수(m), 메시지를 보내고자 하는 도시(c)에 대해서 입력
n, m, start = map(int, input().split())
# 각 노드에 연결되어 있는 정보 담는 리스트 만들기
graph = [[]for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z
    graph[x].append((y, z))

# 다익스트라 알고리즘 
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]: # now에서 시작
            cost = dist + i[1] # dist는 start에서 now까지의 값
                               # i[1]은 now 노드에서 i[0]까지의 값
            if cost < distance[i[0]]: # distance[i[0]]은 start ~ i[0]까지의 값 (초기값 = INF)
                distance[i[0]] = cost # distanc의 경우 최초에 INF 값이므로 값이 최소값으로 수정됨
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

count = 0
result = []

# 모든 노드로 가기 위한 최단거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한 (INFINITY)이라고 출력
    if distance[i] > 0 and distance[i] < INF:
        count += 1
        result.append(distance[i])

print(count, max(result))
