# n 입력받음
n = int(input())

# 여행가 A가 이동할 계획서의 내용
plans = list(map(str, input().split()))

# 최초의 좌표 등록
x, y = 1, 1

# L, R, U, D 이동에 따른 좌표 변동사항 등록
dx = [0, 0, -1, 1] # U, D
dy = [-1, 1, 0, 0] # L, R

# L, R, U, D 파악을 위한 리스트
moves = ['L', 'R', 'U', 'D']

# for 문을 이용한 좌표 이동
for plan in plans:
    for i in range(len(moves)):
        if plan == moves[i]:
            # 임시 저장을 위한 nx, ny 변수 생성
            nx = x + dx[i]
            ny = y + dy[i]
    # if nx <1 or nx > 5 or ny < 1 or ny > 5:
    #     continue
    # else:
    #     x = nx
    #     y = ny
    # 위나 아래나 똑같음 
    if nx >= 1 and nx <= 5 and ny >=1 and ny <= 5:
        x = nx
        y = ny

print(x, y)
