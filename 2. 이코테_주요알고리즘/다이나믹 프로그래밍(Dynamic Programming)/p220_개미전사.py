# 식량창고 N 입력
n = int(input())
# 식량창고에 저장된 식량개수 k 입력
k = [0] + list(map(int, input().split()))
# 최댓값 저장하는 array 생성
array = [0] * 101 

# 재귀함수로 최대값 저장
array[1] = k[1]
array[2] = max(k[1], k[2])

for i in range(3, len(k)):
    array[i] = max(array[i-1], array[i-2] + k[i])

print(array[n])

# ------------------------------------------------
""" 정답 """
""" 다만 코드 입력시 인덱싱 헷갈릴 수가 있어서 그 부분을 유의하면서 입력, 변수명 포함 """
""" 내가 적은 답은 인덱싱 고려않고 순서로 맞춤 / 답변은 인덱싱을 우선으로 작성 """
# 정수 N을 입력받기
n = int(input())
# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# Dynamic Programming 진행 (Bottom up)
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

# 계산된 결과 출력
print(d[n - 1])