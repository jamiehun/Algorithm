# n, k = map(int, input().split())
# count = 0

# while True:
#   if n == 1:
#     break 
  
#   if n % 5 == 0:
#     n /= 5
#     count += 1
#   else:
#     n -=1
#     count += 1

# print(count)

# --------------------------------------
# 모범답안 (위에꺼보다 시간복잡도 줄이는 답안 but, 이해가 어려움)
# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True:
  # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
  target = (n // k) * k # target = 25
  result += (n - target) # result = 0
  n = target # n = 25

  # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k: # 25 < 5
    break 
  # K로 나누기 
  result += 1 # 0 += 1 => 1
  n //= k # n = 

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
print(n)
print(target)
print((25 // 5)*5)