# # <2> 1로 만들기 (p.217)
# # while은 무엇이 아닐때! 사용
# # 첫번째 줄에 정수 x를 입력
# x = int(input())

# # n = x가 될 때까지 while 문 반복
# n = 1
# count = 0

# while (n != x):
#     if x >= (n * 5): # a 연산
#         n *= 5
#         count += 1
#         continue
    
#     elif x >= (n * 3): # b 연산
#         n *= 3
#         count += 1
#         continue

#     elif x >= (n * 2): # c 연산
#         n *= 2
#         count += 1
#         continue

#     elif x >= (n * 1): # d 연산
#         n += 1
#         count += 1
#         continue

# print(count)

# # # --------------------------------------
# # 모범답안
# # (아직까지는 실전에서 이렇게 코딩을 하지는 못할거 같다.. ㅜ) --> 좀더 연습 필요!
# # 정수 x를 입력받기
# x = int(input())

# # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
# d = [0] * 30001

# # 다이나믹 프로그래밍 (Dynamic Programming) 진행 (보텀업)
# for i in range(2, x + 1):
#     # 현재의 수에서 1을 빼는 경우
#     d[i] = d[i-1] + 1
#     # 현재의 수가 2로 나누어 떨어지는 경우
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
#     # 현재의 수가 3으로 나누어 떨어지는 경우
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#     # 현재의 수가 5로 나누어 떨어지는 경우
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i // 5] + 1)

# print(d[x])
# # input
# # 26
# # output
# # 3