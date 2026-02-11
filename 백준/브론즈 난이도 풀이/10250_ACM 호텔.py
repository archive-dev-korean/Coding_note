# 연습
T=int(input())
for _ in range(T):
    arr=[]
    a,b,c=map(int,input().split())
    for j in range(1,b+1): # 호수 1호,2호...
        for i in range(1,a+1): # 층수 1층 2층..
            arr.append((i,j)) # (층,호수) -> 각층 1호 부터 차근차근 넣어짐
    # print(arr)
    floor,room=arr[c-1]
    # print(f"{floor}{room:02d}")
    # f 스트링 옵션 인데
    # 0 -> 빈자리 0으로 채워라
    # 2 -> 최소 2자리로 만들어라
    # d -> 정수

    # 또는
    if room < 10:
        print(str(floor) + "0" + str(room))
    else:
        print(str(floor) + str(room))