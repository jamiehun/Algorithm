# 6086 : [기초-종합] 거기까지! 이제 그만~(설명)(py)
a = int(input())
s = 0
n = 0

while True:
  s += n 
  n += 1
  if s >= a :
    break 

print(s) 

# --------------------------------------------------------
# 6087 : [기초-종합] 3의 배수는 통과(설명)(py)

n = int(input())

for i in range(1, n+1):
  if i % 3 == 0:
    continue
  print(i, sep=" ")

# --------------------------------------------------------
# 6088 : [기초-종합] 수 나열하기1(py)

a, d, n = map(int, input().split())

print(a + d * (n-1))

# --------------------------------------------------------
# 6089 : [기초-종합] 수 나열하기2(py)

a, r, n = map(int, input().split())

print(a * (r ** (n-1)))

# --------------------------------------------------------
# 6090 : [기초-종합] 수 나열하기3(py)
a, m, d, n = map(int, input().split())

for _ in range(1, n):
  a = a * m + d

print(a)

# --------------------------------------------------------
# 6091 : [기초-종합] 함께 문제 푸는 날(설명)(py)
a, b, c = map(int, input().split())

d = 1
while d % a != 0 or d % b != 0 or d % c != 0 :
  d += 1

print(d)

# --------------------------------------------------------
# 6092 : [기초-리스트] 이상한 출석 번호 부르기1(설명)(py)
n = int(input())
a = input().split()

for i in range(n):
  a[i] = int(a[i])

d = []
for i in range(24):
  d.append(0)

for i in range(n):
  d[a[i]] += 1

for i in range(1, 24):
  print(d[i], end=' ')

# --------------------------------------------------------
# 6093 : [기초-리스트] 이상한 출석 번호 부르기2(py)
n = int(input())
a = input().split() 

for i in range(1, n+1):
  print(a[-i], end=" ")

# --------------------------------------------------------
# 6094 : [기초-리스트] 이상한 출석 번호 부르기3(py)
n = int(input())
a = map(int, input().split())

print(min(a))


# --------------------------------------------------------
# 6095 : [기초-리스트] 바둑판에 흰 돌 놓기(설명)(py)
# 20 x 20 2차원 리스트 만들기
d = [[0]*20 for _ in range(20)]

# 흰돌이 있는 위치는 1, 없는 위치는 0으로 만들기
n = int(input())
for _ in range(n):
  a, b = map(int, input().split())
  d[a][b] = 1

# 마지막으로 19 x 19로 프린트 하기
for i in range(1, 20):
  for j in range(1, 20):
    print(d[i][j], end=" ")
  print()

# --------------------------------------------------------
# 6096 : 6096 : [기초-리스트] 바둑알 십자 뒤집기(py) **
# 2차원 리스트 만들기
d = [[0]*19 for i in range(19)] # 2차원 리스트 만들때 가장 기초적인 세팅

for i in range(19):
  a = list(map(int, input().split())) 
  d[i] = a

# 10-10 / 12-12 숫자 변경
n = int(input())

for i in range(n):
  x, y = map(int, input().split()) # 정수값으로 치환하는 것 잊지 말기
  
  for j in range(19):
    if d[j][y-1] == 0:
      d[j][y-1] = 1
    else:
      d[j][y-1] = 0 

    if d[x-1][j] == 0:
      d[x-1][j] = 1
    else:
      d[x-1][j] = 0

# 리스트 값 출력
for l in range(19):
  for m in range(19):
    print(d[l][m], end=" ")
  print() 

# --------------------------------------------------------
# 6097 : [기초-리스트] 설탕과자 뽑기(py)
h, w = map(int, input().split())

# 5 x 5 리스트 만들기
a = [[0] * w for _ in range(h)]

# 막대의 개수 n만큼 input
n = int(input())

for _ in range(n):
  l, d, x, y = map(int, input().split()) # 막대길이(l), 방향(d), 좌표(x, y)
  
  for i in range(l):
    if d == 0 : # d = 0 이면 가로, d = 1이면 세로
      a[x-1][y+i-1] = 1
    else : 
      a[x+i-1][y-1] = 1

# 5 x 5 리스트 출력
for k in range(h):
  for v in range(w):
    print(a[k][v], end=" ")
  print()
  
# --------------------------------------------------------
# 6098 : [기초-리스트] 성실한 개미(py)
# 10 x 10 리스트 만들기
d = [[0]*10 for _ in range(10)]

# 10 x 10 리스트 입력값에 맞추기
for i in range(10):
  a = list(map(int, input().split()))
  d[i] = a 

# 시작점은 9로 맞추기
d[1][1] = 9

# 알고리즘 시작
x = 1
y = 1

while True:
  if d[x][y+1] == 0:
    d[x][y+1] = 9
    y += 1

  elif d[x+1][y] == 0:
    d[x+1][y] = 9
    x += 1

  elif d[x][y+1] == 2:
    d[x][y+1] = 9
    break

  elif d[x+1][y] == 2:
    d[x+1][y] = 9
    break

  else:
    break

for i in range(10):
  for j in range(10):
    print(d[i][j], end=" ")
  print()