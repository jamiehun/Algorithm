# 답
n, m = map(int, input().split())
result = []

for i in range(n):
  a = list(map(int, input().split()))
  result.append(min(a))

print(max(result))

# ------------------------------------------------
# 모범답안
# py min() 함수를 이용하는 답안 예시
# n, m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 가장 작은 수 찾기
  min_value = min(data)
  # 가장 작은 수들 중에서 큰 수 찾기
  result = max(result, min_value)

print(result) # 최종 답안 출력

# ------------------------------------------------
# 모범답안 2
# 2중 반복문 구조를 이용하는 답안 예시

# n, m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 가장 작은 수 찾기
  min_value = 10001
  for a in data:
    min_value = min(a, min_value)
  # 가장 작은 수들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result) # 최종 답안 출력