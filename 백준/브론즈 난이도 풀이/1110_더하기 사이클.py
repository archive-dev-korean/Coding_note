# # 연습
# N=list(str(input()))
# # print(N)
# s=0
# cnt=0

# s+=int(N[1] + N[0]) # 첫번째 합
# cnt+=1

#     # new = int(N[1])  + s # 두번째 합
#     # 새로운 수 변수 (첫번쨰 합이 10보다 작을 때)
# if s <10:
#     new = int(N[1]) * 10 + s # 새로운 수
#     s+=new//10 + s
# else:
#     new = s % 10 + s//10

#     # print(s)
#     # if s > 10:
#     #     new = new // 10  + s % 10
#     #     s+=int(new)
#     # print(new)

N = int(input())
x=N
cnt=0
while True:
    a = x // 10 #10의 자리
    b = x % 10 # 1의 자리
    s = a+b
    x = b * 10 + (s % 10)
    cnt+=1
    if x ==N:
        break
print(cnt)

# 1의 자리 10의 자리 sum 각각 하나씩 구하는게 보기 & 이해에 쉬움