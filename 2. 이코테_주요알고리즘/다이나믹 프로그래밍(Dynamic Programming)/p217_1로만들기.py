""" Bottom up 방식으로 구현하는 것이 아직은 어렵다. """
""" 실제로 Bottom up 방식을 어렴풋이 생각했는데 익숙한 Top Down 방식으로 계속해서 밀어붙였다. """
""" 해결방안이 생각나면 끝까지 한번 생각해보는 연습이 좀 더 필요하다. """
# 정수 x 입력
x = int(input())
count = 0

# 반복문 사용하여 정수를 나누기
while x > 1:
    # 5로 나누기
    if x // 5 != 0:
        x //= 5
        count += 1
        continue
    # 3으로 나누기
    elif x // 3 != 0:
        x //= 3
        count += 1
        continue
    # 2로 나누기
    elif x // 2 != 0:
        x //= 2
        count += 1
        continue
    else:
        x -= 1
        count += 1
        continue

print(count)
