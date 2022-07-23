# 회사의 개수(n)와 간선의 개수(m) 입력
n, m = map(int, input().split())
INF = int(1e9) # INF 입력

# 그래프 생성
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 이어져 있는 회사 표시
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 연결된 두 회사의 번호 공백으로 입력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# x(물건 판매)와 k(소개팅 장소)를 순서대로 입력
x, k = map(int, input().split())

print(graph)

distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)

