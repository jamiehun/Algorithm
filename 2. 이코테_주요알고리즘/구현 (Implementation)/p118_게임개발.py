# """ 내 방식대로 디코딩 완성본 """
# """ 모범답안과 함수부분, 동서남북 표시방법만 다름 """
# """ 순서는 모범답안을 조금은 참고하였음 """
# # n x m 맵 생성
# n, m = map(int, input().split())

# # 방문 맵 생성
# visited = [[0] * m for _ in range(n)]

# # a, b, d (좌표 및 바라보는 방향 입력)
# a, b, d = map(int, input().split())

# """ 답안 보고 추가 """
# # 현재 좌표 방문처리
# visited[a][b] = 1


# # 맵 입력
# game_map = []
# for _ in range(n):
#     game_map.append(list(map(int, input().split())))

# # direction에 따른 좌표 변화 저장 (N, E, S, W 순 ; 반시계방향)
# directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# # 함수 설정
# count = 1
# turn_count = 0
# while True:
#     # 시계 반대방향으로 전환하되 인덱스가 4 넘으면 4를 빼줌
#     d += 1
#     if d >= 4:
#         d -= 4

# # """ 순서 변경한 부분 """
# # 방향 전환 후 이동한 것으로 가정

#     da = a + directions[d][0]
#     db = b + directions[d][1]

#     if game_map[da][db] == 0 and visited[da][db] == 0 :
#         a = da
#         b = db
#         visited[a][b] = 1 
#         count += 1
#         turn_count = 0
#         continue

#     else:
#         turn_count += 1

#     if turn_count == 4:
#         # 4번 이상 돌면 뒤로 물러나기
#         da = a - directions[d][0]
#         db = b - directions[d][1]

#         if game_map[da][db] == 0:
#             a = da
#             b = db
    
#         else:
#             break

#         turn_count = 0

# print(count)

# -----------------------------------------------
# 모범 답안
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 x 좌표, y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전 <-- 이 부분이 다름
def turn_left():
    global direction # 전역 변수는 미리 설정해줌
    direction -= 1
    if direction == -1:
       direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸인 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0 and d[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)
