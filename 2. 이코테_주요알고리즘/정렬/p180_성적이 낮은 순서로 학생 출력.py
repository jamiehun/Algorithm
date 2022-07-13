# 학생의 수 N을 입력
n = int(input())

# 두번째 ~ n+1번째까지 학생의 이름과 문자열 구분하여 입력
array = []

for i in range(n):
    a, b = input().split()
    array.append((a, b))

""" lambda 부분을 설정하여 결과값 내는 것이 헷갈렸음(익숙해질 필요가 있음!) """
# array를 정렬하면서 key값도 함께 설정
result = sorted(array, reverse = False, key = lambda x : x[1])

# 순서대로 결과값 출력
# print(result)
for i in result:
    print(i[0], end = " ")