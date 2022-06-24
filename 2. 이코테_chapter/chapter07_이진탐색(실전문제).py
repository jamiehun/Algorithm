# 3. 떡볶이 떡 만들기 (p.201)
# 내가 만든 답안
# 떡의 개수(n)과 요청한 떡의 길이(m)을 입력받기
n, m = map(int, input().split())
# 배열을 새로 만들어서 해당 배열에 각 떡의 남은 값들을 넣을려고 하였음
original = list(map(int, input().split()))
array = [0] * n

# start와 end 만들어서 재귀함수에 쓰기
start_array = array[0]
end_array = array[-1]
mid = (start_array + end_array) // 2

# 재귀함수를 사용한 솔루션 제공
def cutting():
    for i in original
        if (i-mid) < 0:
            array[i] = 0
        else:
            array[i] = i - mid
    if sum(array) > m :
        def cutting(start_array+1) # 여기에서 함수를 제대로 사용하는 법이 생각 안남
    else:
        def cutting(end_array-1) # 위와 동일
# 추후 포기

# -----------------------------------------------------------------
# 7-8. 모범답안
# 떡의 개수 (N)과 요청한 떡의 길이(M)을 입력받기
n, m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로 여기에서 result 기록
        start = mid + 1

# 정답 출력
print(result)

# input
# 4 6
# 19 15 10 17
# ouput
# 15