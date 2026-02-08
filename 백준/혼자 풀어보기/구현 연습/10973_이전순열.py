# 구현 연습
from itertools import permutations
import sys
input=sys.stdin.readline
N=int(input())
result=[]
arr=list(map(int,input().split()))
target=tuple(arr)
# result=[]
# result.append(arr)
# print(arr)
for v in permutations(arr,N):
    # print(v)
    result.append(v)
result.sort()
# print(result)
for i,j in enumerate(result):
    if j == target:
        if i==0:
            print(-1)
        else:
            print(*result[i-1])
        break
# cnt=0
# # print(*arr)
# arr.sort()
# print(arr)
# for i in str(arr):
#     # print(i)
#     arr[0]

# 이렇게 구해도 정답은 나오는데 메모리 초과 뜸.
# 수정 버전
N = int(input())
a = list(map(int, input().split()))

# 1) 뒤에서부터 '내림차순이 깨지는 지점' 찾기
i = N - 1
while i > 0 and a[i-1] <= a[i]:
    i -= 1

if i == 0:
    print(-1)
else:
    # 2) a[i-1]보다 작은 값 중 가장 오른쪽 값 찾기
    j = N - 1
    while a[j] >= a[i-1]:
        j -= 1

    # 3) 스왑
    a[i-1], a[j] = a[j], a[i-1]

    # 4) 뒤쪽(i~끝)을 내림차순으로 만들기 (원래는 오름차순이었으니 reverse면 됨)
    a[i:] = reversed(a[i:])

    print(*a)