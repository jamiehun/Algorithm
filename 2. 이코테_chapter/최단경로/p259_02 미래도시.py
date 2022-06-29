"""문제를 어떻게 풀어야할지에 대해서는 직접 생각하고 코드에 대한 아이디어만 책에서 차용해왔음"""
"""아이디어를 잘 짜서 코드를 구현하는 것도 어렵지 않았음"""
"""코드만 책보고 안 짤 수 있을 정도로 연습하면 될 것 같음"""
# 플로이드 워셜 알고리즘
# 모든 경로의 최소값 구해서 1 -> K -> X의 최소시간 찾기

# n, m 값 입력
n, m = map(int, input().split())
INF = 1e9

# (n + 1) x (n + 1) 그래프 생성
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에게 가는 것은 0으로 설정
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# a -> b의 값 차례대로 입력 (연결된 회사는 양방향으로 이동 가능)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# a -> k -> b의 최소값 구해서 graph에 저장
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# x(판매회사)과 k(소개팅 회사)값 입력 받기
x, k = map(int, input().split())

# 최종적인 값 출력
min_time = graph[1][k] + graph[k][x]

if min_time >= INF:
    print(-1)
else:
    print(min_time)