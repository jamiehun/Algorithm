""" 이진탐색을 사용하여 풀었지만 실제로는 틀린 답변일 수 있다."""
""" 설정할 수 있는 높이의 최대값을 구하라고 했지만 해당 답변에서는 """
""" 19번째 줄에서 볼 수 있는 것처럼 값이 딱 떨어질때만 결과값이 print되기 때문 """
""" 또한 sort를 굳이 하지 않아도 되는데 나의 이해도를 위해서 sort를 진행하였다 """
""" 좀 더 간결하고 정확한 소스코드 구현이 중요하다. """
""" 이진탐색을 활용해서 해당 문제를 풀어낼려고 한 점, 제 시간에 테스트케이스에 맞게 구현한 점은 잘했다. (연습이 중요!)"""

# 이진탐색 함수 만들기
def binary_search(array, m, start, end):
    # start > end이면 None
    if start > end:
        return None
    # mid(중간값으로 절단기 높이에 쓸 예정) 구하기
    mid = (start + end) // 2
    # result 구하기 (전체 array 요소들 중 mid만큼 잘라서 나머지 sum)
    result = sum([(i-mid) for i in array if (i-mid > 0)])
    
    # 구한 result 값과 목표값인 m이 일치하면 mid(절단기 높이) 출력
    if result == m:
        return mid
    # result 값이 목표값인 m보다 적으면 너무 많이 잘랐다는 것이므로 절단기 높이를 낮춰서 진행
    elif result < m:
        return binary_search(array, m, start, mid - 1)
    # result 값이 목표값인 m보다 크면 너무 적게 잘랐다는 것이므로 절단기 높이를 높여서 진행
    else:
        return binary_search(array, m, mid+1, end)

# n(떡의 개수)와 m(요청한 떡의 길이) 입력
n, m = map(int, input().split())

# 떡의 개별 높이 입력 후 오름차순으로 정리
array = list(map(int, input().split())) 
array.sort()

# 최종 값 구현
max_height = binary_search(array, m, array[0], array[-1])
print(max_height)
