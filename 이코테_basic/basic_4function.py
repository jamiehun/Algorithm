# 함수의 더하기
def add(a, b):
  return a + b
print(add(3, 7))
print()

# --------------------------------
# return 문 없이 작성
def add(a, b):
  print('함수의 결과:', a + b)

add(3, 7)
print()

# --------------------------------
# 파라미터의 변수를 직접 지정해서 값을 넣기
def add(a, b):
  print('함수의 결과:', a + b)
add(b = 3, a = 7)
print()

# --------------------------------
# global 함수를 활용하여 변수 데이터 변경
a = 0

def func():
  global a
  a += 1

for i in range(10):
  func()

print(a)
print()

# --------------------------------
# 람다를 활용한 함수 표현
def add(a, b):
  return a + b

# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a+ b)(3, 7))