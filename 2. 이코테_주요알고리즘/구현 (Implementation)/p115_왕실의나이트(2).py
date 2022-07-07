""" 오답의 이유 : ord(a)가 떠오르지 않았음 """
""" 리스트 말고 튜플 형태로도 답안 작성할 수 있게끔 연습 필요! """
# 좌표를 나타내는 문자열 입력
n = input()

# 8가지의 옵션 제공
options = ["RRU", "RRD", "LLU", "LLD", "UUR", "UUL", "DDR", "DDL"]

# 행과 열 설정
x = int(n[1])
y = int(ord(n[0])-96)

# L, R, U, D 움직임 설정하기
dx = [0, 0, -1, +1]
dy = [-1, +1, 0, 0]
moves = ["L", "R", "U", "D"]

count = 0

for option in options:
    nx = x
    ny = y
    for i in option:
        for j in range(len(moves)):
            if moves[j] == i:
                nx = nx + dx[j]
                ny = ny + dy[j]
    if nx <= 8 and nx >= 1 and ny <= 8 and ny >= 1:
        count += 1

print(count)

#----------------------------------------------------------------------------
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]) - int(ord('a'))) + 1 """ 틀린 위치 """

""" 간단하게 표현할 수 있는 부분 """
# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

""" 위의 코드보다 훨씬 간결하고 명확함"""
# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동 후 조건에 맞다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_row <= 8:
        result += 1

print(result)