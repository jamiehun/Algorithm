# 이진탐색 함수 작성
def binary_search(array, target, start, end):
    if start > end:
        return None
    # 중간값 작성
    mid = (start + end) // 2
    # 찾는 값이 중간 값과 같으면 값 리턴
    if array[mid] == target:
        return mid
    # target이 mid 값보다 작을 때
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    # target이 mid 값보다 클때
    else:
        return binary_search(array, target, mid+1, end)
    
# 부품(n)과 부품의 종류(array) 입력
n = int(input())
array = list(map(int, input().split()))

# array 정렬
sorted(array)

# 찾으려는 부품 개수와 찾으려는 부품 종류 입력
m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    result = binary_search(array, target, 0, n-1)
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
