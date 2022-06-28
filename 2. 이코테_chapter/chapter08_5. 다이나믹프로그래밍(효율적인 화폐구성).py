# 문제의 정의 : n가지의 종류의 화폐, m은 만들려는 화폐의 금액
# 문제의 핵심 : m이라는 화폐를 만들 때 최소한의 방법 수를 a(m)이라고 한다
#            n가지 종류의 화폐를 하나씩 꺼내보며 (i) a(m-i)와 a(m)간의 최소값을 비교함            

# 의사코드
# 정수 N과 M을 입력받기
# N개의 화폐 단위 정보를 입력받아 리스트에 저장 : array
# 한번에 계산된 결과를 저장하기 위해 새로운 리스트 저장 : d => 10001
# d가 0일때부터 체크하며 array에 있는 리스트 값을 하나씩 빼어서
# d[j - array[i]] + 1와 d[j] 간의 최소값을 비교하며 d를 업데이트 함
# d에 값 변화가 없을 때는 -1을 출력하고 있을 때는 해당 값을 입력
# ----------------------------------------------------------

# 정수 N과 M을 입력받기
n, m = map(int, input().split())

# N개의 화폐를 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

# 한번에 계산된 결과를 저장하기 위해 새로운 리스트 저장
d = [10001] * (m + 1)

# d가 0일때부터 체크하며 array에 있는 리스트 값을 빼내며 확인
d[0] = 0
for j in range(n):
    for k in range(array[j], m + 1):
        d[k] = min(d[k], d[k - array[j]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])