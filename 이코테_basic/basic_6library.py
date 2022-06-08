# 내장함수
# sum 함수
result = sum([1, 2, 3, 4, 5])
print(result)

# min 함수
result = min(7, 3, 5, 2)
print(result)

# max 함수
result = max(7, 3, 5, 2)
print(result)

# eval 함수
result = eval("(3 + 5) * 7" )
print(result)

# sorted 함수
result = sorted([9, 1, 8, 5, 4]) # 오름차순으로 정렬
print(result)

result = sorted([9, 1, 8, 5, 4], reverse = True) # 내림차순으로 정렬
print(result)

# key 속성을 내림차순 정렬 (튜플)
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], 
               key = lambda x : x[1], reverse = True )
print(result)

# sort() 함수를 사용해서 정렬
data = [9, 1, 8, 5, 4]
data.sort()
print(data)
print()

# ---------------------------------------------------------------------
# permutations (순열)
from itertools import permutations

data = ['A', 'B', 'C'] # 데이터 준비
result = list(permutations(data, 3))

print(result)

# combinations (조합)
from itertools import combinations

data = ['A', 'B', 'C'] # 데이터 준비
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기

print(result)

# product (중복을 허용하는 순열)
from itertools import product
data = ['A', 'B', 'C'] # 데이터 준비
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용))
print(result)
print()

# combinations_with_replacement (중복을 허용하는 조합)
from itertools import combinations_with_replacement
data = ['A', 'B', 'C'] # 데이터 준비
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복허용))
print(result)
print()

# ---------------------------------------------------------------------
# heapq 활용
import heapq 

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for _ in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
print()

# ---------------------------------------------------------------------
# heapq 최대 힙으로 사용
import heapq

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, -value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for _ in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
print()

# ---------------------------------------------------------------------
# bisect
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
# print()

# ---------------------------------------------------------------------
# count_by_range
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)
  return right_index - left_index

# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))
# print()

# ---------------------------------------------------------------------
# collections - deque
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data)) # list 자료형으로 변환
# print()

# ---------------------------------------------------------------------
# collections - Counter 
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])  # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'이 등장한 횟수 출력
print(dict(counter))    # dictionary 자료형으로 변환
# print()

# ---------------------------------------------------------------------
# math - factorial
import math
print(math.factorial(5)) # 5 팩토리얼 출력

# math - sqrt
import math
print(math.sqrt(7)) # 7의 제곱근을 출력

# math - gcd (최대공약수, Greatest Common Divisor)
import math
print(math.gcd(21, 14))

# math - pi, e (파이, 자연상수)
import math 
print(math.pi) # 파이(pi) 출력
print(math.e)  # 자연상수 e 출력
