# p.92 큰 수의 법칙

N, M, K = map(int, input().split()) # N:배열의크기, M:더해지는횟수, K: ~번

# 두번째 입력 값 리스트로 받기
a = list(map(int, input().split()))

# a 리스트 내림차순으로 정렬하기
a.sort(reverse=True)

# 큰 수의 법칙 사용하기
count = 0
n = 0 

while M > 0:
  for i in range(K):
    if M == 0:
      break 
    count += a[n]
    M -= 1
  if a[n] > a[n+1]:
    count += a[n+1]
    M -= 1
  else:
    pass

print(count)

# 해설
# 모범답안과는 다르지만 전체적인 맥락은 같다.
# 처음에 사용한 구절은
# 31 라인에서 
# for i in range(K):
#   count += a[n]
#   M -= 1
# 이거였는데 for이 돌아가는 동안에는 M이 음수여도 막지를 못했다.
# 답안에서 표현해준 if ~ break 구문 덕분에 문제가 풀렸다.

# ----------------------------------------------------
# 모범답안
n, m, k = map(int, input().split())
# n 개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort(reverse=True) # 입력받은 수를 정렬하기
first = data[0]
second = data[1] 

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k
count += m % (k + 1)

result = 0
result += count * first 
result += (m-count) * second 

print(result)