# 정수 n 입력받기
n = int(input())

# hh, mm, ss로 나누어서 for 문으로 해당사항 찾기
count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            # if '3' in str(h) or str(m) or str(s):
            # 왜 위의 값은 안될까?
            if '3' in str(h) + str(m) + str(s) :
                count += 1

print(count)