# N, M, K 입력받기
n, m, k = map(int, input().split())

# array 입력받기
array = list(map(int, input().split()))

# array를 내림차순으로 정렬
array.sort(reverse=True)

# 몫과 나머지 정리
quotient = m // (k+1)
remainder = m % (k+1)

# 값 구하기
result = (array[0] * k + array[1]) * quotient +\
            (array[0]) * remainder

print(result)

