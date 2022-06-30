""" 문제를 풀기는 풀었으나 아래의 정석적인 답변이 나올정도는 안됐다. """
""" 정석적인 답변도 바로 나올 수 있게끔 지속적인 연습이 필요하다. """

# N과 K를 각각 입력 받음
n, k = map(int, input().split())
count = 0

# 1이 될 때까지 연산 수행
while n > 1:
    if n % k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)

# ----------------------------------
# 정석적인 답변 (시간복잡도 때문에)
# n, k 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += n - target
    n = target

    # N이 K 이하면 반복문 종료
    if n < k:
        break

    result += 1
    n //= k

# 남아있는 수 마저 정리하기
result += (n - 1)
print(result)

