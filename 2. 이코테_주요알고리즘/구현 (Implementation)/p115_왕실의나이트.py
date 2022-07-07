# a ~ h까지 숫자 넣어주기
a = input()
row = int(a[1])
col = int(ord(a[0]) - ord("a")) + 1

# print(col)

steps = [[1, 2], [-1, 2], [1, -2], [-1, -2],
         [2, 1], [2, -1], [-2, 1], [-2, -1]]

count = 0 
# b = list()

for i in steps:
  dx = row
  dy = col 
  
  dx += i[0]
  dy += i[1]
  
  if (dx >= 1 and dx <= 8) and (dy >= 1 and dy <= 8):
    count +=1  
    # print(dx)
    # print(dy)
    # print()
    # b.append(i)

print(count)
# print(b)

# ---------------------------------------------
# 모범답안
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
# 여기에서 문자를 숫자로 바꿔주는 ord가 중요함

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
# 튜플의 경우 인덱싱이 가능하며, 해당 값을 인덱싱을 통해 변경하는 것은 안된다. 

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:

  # 이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_column = column + step[1]

  # 해당 위치로 이동이 가능하다면 카운트 증가
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_row <= 8:
    result += 1

print(result)