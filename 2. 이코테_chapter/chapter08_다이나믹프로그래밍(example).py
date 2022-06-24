# 8-1. py 피보나치 함수 소스코드
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))

# -------------------------------
# 8-2. py 피보나치 수열 소스코드 (재귀적)
# 한번 계산된 결과를 메모제이션(memozation)하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수 (Fibonacci Function)를 재귀함수로 구현 (탑다운 다이나믹 프로그래밍)
def fibo(x):
    # 종료조건 (1 혹은 2일때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 변환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))

# -------------------------------
# 8-3. py 호출되는 함수 확인
d = [0] * 100

def pibo(x):
    print('f(' + str(x) + ')', end= ' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]

pibo(6)

# -------------------------------
# 8-4. py 피보나치 수열 소스코드(반복적)
# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수를 반복문으로 구현 (bottom-up 다이나믹 프로그래밍)
for i in range(3, n + 1):
    d[i] = d[i-1] + d[i-2]

print(d[n])
218922995834555169026