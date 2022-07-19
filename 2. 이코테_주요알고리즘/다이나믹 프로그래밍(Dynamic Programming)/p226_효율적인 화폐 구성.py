""" 답안은 array에서 하나씩 꺼내서 값을 넣은 후 """
""" array 값별로 m에 이를 때까지 숫자 적어넣으면서 최소값 구하는 것 """
""" d를 10001로 넣어두면서 최소값과 비교하고 전에 값이 있는지 알아가는 과정이 새로웠음 """

# n(화폐의 개수), m(목표값) 입력하기
n, m = map(int, input().split())

# array 입력
array = list(map(int, input().split()))
d = [0] * 10001
 
def count():
    for i in array:
        d[i] = 1

    for j in array:
        count(m) = count(m-j) + 1

    return d[m]

result = count(m)
