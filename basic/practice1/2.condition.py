# # 아무 것도 처리하고 싶지 않을 때 pass
# score = 85

# if score >= 80:
#   pass # 나중에 작성할 코드
# else:
#   print('성적이 80점 미만입니다.')

# print("프로그램을 종료합니다.")
# print()

# # ---------------------------------------------
# # 줄 바꿈을 하지 않고 간단하게 표현
# score = 85

# if score > 80: result = "Success"
# else: result = "Fail"

# print(result)
# print()

# ---------------------------------------------
# 조건문 표현식 사용
score = 85
result = "Success" if score >= 90 else "Fail"

print(result)
print()

# ---------------------------------------------
# 특정 원소 값을 없애는 조건문
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []
for i in a:
  if i not in remove_set :
    result.append(i)

print(result)
print()

# ---------------------------------------------
# 특정 원소 값을 업애는 조건문 (좀 더 간결하게)
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)
print()

# ---------------------------------------------
