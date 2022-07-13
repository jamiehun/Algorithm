# n개의 원소와 k개의 바꿔치기 개수를 설정
n, k = map(int, input().split())

# 배열 A와 배열 B의 값을 입력
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

# 배열 A는 오름차순으로, 배열 B는 내림차순으로 정렬
sorted_a = sorted(array_a)
sorted_b = sorted(array_b, reverse = True)


# 배열 A와 B의 바꿔치기 수행
for i in range(k):
    if sorted_a[i] < sorted_b[i]:
        sorted_a[i], sorted_b[i] = sorted_b[i], sorted_a[i]

# 합계 출력
print(sum(sorted_a))
