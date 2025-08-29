T = int(input().strip())

for tc in range(1, T + 1):
    N, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    sub = sorted(arr[s-1:e])   # s~e 구간(1-based)을 잘라 정렬
    ans = sub[k-1]             # k도 1-based라 인덱스는 k-1
    
    print(f"#{tc} {ans}")

f스트링과 슬라이싱 활용
