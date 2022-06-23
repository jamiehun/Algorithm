# 10억의 지수 표현방식
a = 1e9
print(a)

# 752.5
a = 75.25e1
print(a)

# 3.954
a = 3954e-3
print(a)
print( )

# --------------------------------
# 0.9를 제대로 인식 못하는 문제
a = 0.3 + 0.6 
print(a)

if a == 0.9:
  print(True)
else:
  print(False )
print()

# --------------------------------
# round 사용하여 0.9를 제대로 인식시킴
a = 0.3 + 0.6
print(round(a, 4))

if round(a, 4) == 0.9:
  print(True)
else:
  print(False)
print()

# --------------------------------
# 빈 리스트 선언 방법 1)
a = list()
print(a)

b = []
print(b)
print()

# --------------------------------
# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)
print()

# --------------------------------
# 리스트 컴프리 핸션
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)

# N x M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

# N x M 크기의 2차원 리스트 초기화 (잘못된 방법)
n = 3 
m = 4 
array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array)

# 리스트 컴프리핸션을 사용하여 위의 방법 test
n = 3
m = 4
array =[[0] * m for _ in range(n)]
print(array)

array[1][1] = 5
print(array)
print()

# --------------------------------
# 리스트 관련 기타 메서드
a = [1, 4, 3]
print("기본 리스트:", a)

# 리스트에 원소 삽입
a.append(2)
print("삽입: ", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬: ", a)

# 내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬: ", a)

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기:", a)

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3 추가: ", a)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)
print()

# --------------------------------
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)
print()

# --------------------------------
# 백슬래시(\)를 사용하여 따옴표 원하는 만큼 포함시키기
data = 'Hello World'
print(data)

data = "Don't you know \'Python\'?"
print(data) 
print()

# --------------------------------
# 문자열 데이터의 슬라이싱
a = "ABCDEF"
print(a[2 : 4])
print()

# --------------------------------
# 튜플 : 대입연산자를 사용하여 값을 변경 불가
a = (1, 2, 3, 4)
print(a)

a[2] = 7
print()

# --------------------------------
# dictionary를 사용하는 것
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

if '사과' in data:
  print("'사과'를 key로 가지는 데이터가 존재합니다.")
  print()

# --------------------------------
# 사전 자료형 관련 함수
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()

# 값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
  print(data[key])
  print()

# --------------------------------
# 집합 자료형 초기화 방법 1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 자료형 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)
print()

# --------------------------------
# 집합 자료형의 연산
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합
print()

# --------------------------------
# 집합 자료형 관련 함수
data = set([1, 2, 3])
print(data) 

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러개 추가
data.update([5, 6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)
