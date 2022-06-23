# n = int(input())

# if n < 3 :
#   result = 15 * 15 * (n + 1)
# else :
#   result = (60 * 60) + (15 * 15 * n)

# print(result)
# 오답 이유 
# : 컴퓨팅 사고를 하지 않고 (컴퓨터가 직접 풀게 만들지 않고) 
#   오히려 내가 경우의 수를 찾아서 컴퓨터에게 심어줄려고 하였음
# -----------------------------------------
# 모범 답안
# h를 입력받기
h = int(input())
count = 0

for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)