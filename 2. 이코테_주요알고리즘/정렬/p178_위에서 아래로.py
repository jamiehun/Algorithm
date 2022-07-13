# 수열에 속해있는 수의 개수 입력받기
n = int(input())

# 두번째 줄부터 n+1번째 줄까지 N개의 수 입력
array = []

for i in range(n):
    a = int(input())
    array.append(a)

# array 내림차순으로 정렬하기
array.sort(reverse=True)

# array를 하나씩 꺼내어 출력
for i in array:
    print(i, end = " ")
