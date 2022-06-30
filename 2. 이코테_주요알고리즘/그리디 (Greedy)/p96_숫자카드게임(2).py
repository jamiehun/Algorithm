""" (1)에서는 최소값의 리스트를 만들어 그 중 max 값을 구했음 """
""" (2)에서는 리스트를 하나씩 받아서 min 중 max 값을 구했음 """
""" 시간복잡도는 하나씩 받는거라 크게 차이가 없을 것 같다 O(N)인듯? """

# n, m 숫자 입력 받기
n, m = map(int, input().split())

# array로 각 행의 숫자들을 입력
array = []

for _ in range(n):
    array.append(list(map(int, input().split())))


min_total = 0

for i in range(n):
    min = 10001
    for j in range(m):
        if array[i][j] < min:
            min = array[i][j]
    if min > min_total:
        min_total = min

print(min_total)

# --------------------------------------
""" 첫번째 시도 ('int' object is not collable 오류 발생) """
""" 해당 오류는 min이라는 변수를 설정함과 동시에 min 함수를 사용해서 그렇다. """
""" 아래는 디버깅 완료한 코드 """
# 리스트를 한줄씩 뽑아서 최저값을 받아내고 그 최저값 중 max를 result로 인식시킴

result = 0

for i in range(n):
    min_data = min(array[i])
    result = max(result, min_data)

print(result)