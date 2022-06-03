# 입력을 위한 전형적인 소스코드
# 데이터 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split())) # split()은 입력값(공백, 콤마) 기준으로 분리 
data_comma = list(map(int, input().split(',')))
data_comma_space = list(map(int, input().split(',')))

data.sort(reverse=True)
data_comma.sort(reverse=True)
data_comma_space.sort(reverse=True)

print(data)
print(data_comma)
print(data_comma_space)
print()

# --------------------------------
공백을 기준으로 구분하여 적은 수의 데이터 입력
n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())

print(n, m ,k)
print()

# --------------------------------
# readline() 사용 소스코드 예시
import sys
data = sys.stdin.readline().rstrip()
print(data)
print()

# --------------------------------
# 변수 출력 예시
# 출력할 변수들
a = 1
b = 2

print(a, b)
print()

# --------------------------------
# 출력 줄 바꿈 예시
a = 1
b = 2

print(a)
print(b)
print()

# --------------------------------
# 출력 시 오류가 발생하는 소스코드 예시
# 출력할 변수들
answer = 7

print("정답은 " + answer + "입니다.")
print()

# --------------------------------
# 변수를 문자열로 바꾸어 출력하는 소스코드 예시
# 출력할 변수들
answer = 7

print("정답은 " + str(answer) + "입니다.")
print()

# --------------------------------
# 각 변수를 콤마(,)로 구분하여 출력하는 소스코드 예시
# 출력할 변수들
answer = 7

print("정답은", answer , "입니다.")
print()

# --------------------------------
# f-string 문법을 사용
answer = 7
print(f"정답은 {answer}입니다.")