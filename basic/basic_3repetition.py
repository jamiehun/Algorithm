# # while 문 기초
# i = 1
# result = 0

# # i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
# while i <= 9:
#   result += i
#   i += 1

# print(result)
# print()

# # --------------------------------
# # 1 ~ 9 까지 홀수 값만 더하기
# i = 1
# result = 0

# # i가 9보다 작거나 같을 대 아래 코드를 반복적으로 실행
# while i <= 9:
#   if i % 2 == 1:
#     result += i
#   i += 1

# print(result)
# print()

# # --------------------------------
# # for 문 기초
# result = 0

# # i는 1부터 9까지의 모든 값을 순회
# for i in range(1, 10):
#   result += i

# print(result)
# print()

# # --------------------------------
# # for 문 기초(2)
# scores = [90, 85, 77, 65, 97]

# for i in range(5):
#   if scores[i] >= 80:
#     print(i + 1, "번 학생은 합격입니다.")
# print()

# # --------------------------------
# continue를 사용하여 cheating 걸러내기
scores = [90, 85, 77, 65, 97]
cheating_list = {2, 4}

for i in range(5):
  if i + 1 in cheating_list:
    continue
  if scores[i] >= 80:
    print(i + 1, "번 학생은 합격입니다.")
print()

# --------------------------------
