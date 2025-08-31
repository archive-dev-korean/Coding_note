# 예를 들어 배열이
arr = [5,3,7,9,2,5,2,6] 
#이 중에서 최솟값을 구하고 싶을 떄
arrMin = float('inf') #float('inf')는 무한히 큰 수 임 inf= infinite
for i in range(len(arr)):
  if arr[i]<arrMin:
    arrMin=arr[i]
print(arrMin)
#하면 arrMin이 최대로 큰 값이니까 arr배열의 첫번째 숫자부타 무한대와 비교함 -> 당연히 작으니 무조건 첫째 수가 arrMIn=arr[i]에 포함됨\
#루프 돌기 때문에 그다음수와 비교해서 더 작은수를 대입하는 개념임. 즉, 배열의 원소중에 최솟값이 모든 원소와 비교해서 대입됨.

#다른 방식으로는
for x in arr:
  if x<arrMin:
    arrMin=x
print(arrMin)
#하면 똑같음 그냥 다른 형태로 쓴것임.

#또 다른 방식으로는
arrMin=arr[0]
for i in range(1, len(arr)):
  if arr[i]<arrMin:
    arrMin=arr[i]
print(arrMin)

#이거는 배열의 첫번째 숫자를 지정해서 배열의 첫번째 수와 모든 수를 비교하는 것 결과는 같음


