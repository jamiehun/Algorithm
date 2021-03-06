# 정렬
### 데이터를 특정한 기준에 따라서 순서대로 나열하는 것
### 선택정렬, 삽입정렬, 퀵정렬, 계수정렬 등 (추후 이진탐색 가능)

</br>

## 선택정렬 (Selection Sort)
### 원리
- 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고 그 다음 똑같이 반복 (가장 원시적인 방법)
- *시간복잡도는 O(N**2)* ; 2중 반복문의 사용

</br>

## 삽입정렬 (Insertion Sort)
### 원리
- 특정한 데이터가 적절한 위치에 들어가기 이전에 그 앞까지의 데이터는 이미 정렬되어 있다고 가정하고 적절한 위치를 찾아 삽입
- 거의 정렬되어 있는 상태라면 매우 빠르게 동작함
- *시간복잡도는 O(N**2)* ; 2중 반복문의 사용

</br>

## 퀵정렬 (Quick Sort)
## 호어 분할 (Hoare Partition)
### 원리 
- 리스트에서 첫번째 데이터를 피벗으로 정함
- 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾음 (엇갈리면 피벗과 작은데이터를 바꿈)
- 최종적으로는 왼쪽에는 피벗보다 작은 데이터가 위치하고 오른쪽에는 피벗보다 큰 데이터가 위치함 (분할 (Divide) 혹은 파티션 (Partition)이라 부름)
- *시간복잡도는 O(NlogN)* ; 분할이 이루어지는 횟수가 기하급수적으로 감소함, but 최악의 경우는 O(N**2)

</br>

## 계수정렬 (Count Sort)
### 원리 
- 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
    - 최악의 경우에도 *시간복잡도가 O(N + K)임*
    - 데이터의 개수 : N, 데이터 중 최댓값 : K
    - 앞에서부터 데이터를 하나씩 확인 + 리스트 각 인덱스에 해당하는 값 확인할 때 데이터 중 최댓값만큼 반복
- 계수정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능 (실수는 사용이 어려움)
- 일반적으로 가장 큰 데이터와 가장 작은 데이터 차이가 1,000,000을 넘지 않을때 효과적으로 사용 가능
- 때에 따라서는 비효율을 초래할 수 있는데 예를 들어서 0과 999,999 2개만 존재할 때
- 따라서 동일한 값을 가지는 데이터가 여러개 등장할 때 적합함
- 데이터의 크기 한정되어 있고 데이터의 크기가 많이 중복되어 있을 때!

</br>

## 파이썬의 정렬 라이브러리
### 종류
- *sorted()*
    - 퀵정렬과 동작방식이 비슷한 병합 정렬을 기반으로 만들어짐
    - 병합정렬은 일반적으로 퀵정렬보다 느리나 최악의 경우에도 *시간 복잡도는 O(NlogN)을 보장*
- *sort()*
    - 내부 원소를 바로 정렬함으로써 별도의 정렬된 리스트를 반환하지 않음
- sorted()나 sort()에 key 매개변수를 입력으로 받을 수 있으며 key 값으로는 하나의 함수가 들어가야 정렬 기준이 됨

### 시간복잡도
- 정렬라이브러리는 최악의 경우에도 O(NlogN)을 보장함
- 문제에서 별도의 요구가 없이 단순 정렬해야하는 경우에는 기본 정렬 라이브러리를 사용
- 데이터의 범위가 한정되어 있으며 더 빠르게 동작해야할 때는 계수 정렬을 사용

</br>

## 문제유형
1. 정렬 라이브러리로 풀 수 있는 문제 : 기본 정렬 숙지
2. 정렬 알고리즘 원리에 대해 물어보는 문제 : 선택 정렬, 삽입 정렬, 퀵 정렬 등의 원리를 알고 있어야 함
3. 더 빠른 정렬이 필요한 문제 : 퀵 정렬 기반의 정렬 기법으로는 풀 수 없으며 다른 알고리즘이나 기존 알고리즘의 개선필요