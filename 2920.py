# 정렬 팁
# sort 함수는 원본을 변경 / sorted 함수는 사본을 변경해 반환

arr = list(map(int, input().split(' '))) # 공백을 기준으로 int형의 변수를 입력받아 배열로 저장

if (arr == sorted(arr)): # 배열 arr가 오름차순임을 확인
    print("ascending")
elif (arr == sorted(arr, reverse=True)): # 배열 arr가 내림차순임을 확인
    print("descending")
else: # 둘다 아니면 mix
    print("mixed")