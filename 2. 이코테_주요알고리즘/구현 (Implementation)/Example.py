# 맵의 크기 표시
n, m = map(int, input().split())

# 서있는 위치와 방향 표시
a, b, d = map(int, input().split())

map_info = []
visited = [[a, b]]

# 맵의 상태 표시
for _ in range(n):
  info = map(int, input().split())
  map_info += info

# 반 시계 방향으로 돌리기
direction = [0, 1, 2, 3]
steps = [[-1, 0], [0, 1], [1, 0], [0, -1]]
count = 0 # 돌아본 횟수

while True:
  d = direction[d-1]
  a += steps[d][0] 
  b += steps[d][1]

  if [a, b] in visited or map_info[a][b] == 0:
    a -= steps[d][0]
    b -= steps[d][1] 
    count += 1
  
    if count == 4 :
      a -= steps[d][0]
      b -= steps[d][1]
      if map_info[a][b] == 0:
        break

  else: 
    visited.append([a, b])
    count = 0 