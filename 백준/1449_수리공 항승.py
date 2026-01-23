# 마찬가지 Greedy를 이용한 풀이
N,L = map(int,input().split())
# p=[]
answer=0
# for _ in range(N):
#     p.append(int(input()))

# 내 풀이
# for i in p:
#     for j in range(i+1,p+1):
#         if abs(j-i > L-1):
#             pass
#         else:
#             answer+=1

# 정답 풀이 
# False 배열을 만들어서 구멍이 나 있는 곳에서만 True로 바꾸고
# x 변수를 사용해서 다음 위치값 coord에 저장 및 반복해서 answer 값 증가 시킴
# 정답은 answer의 개수 리턴하면 됨 x에 만 테이프를 붙이는 것이기 때문.

# coord = [False] * 1001
# for i in map(int, input().split()):
#     coord[i] = True
# x = 0
# while x <1001:
#     if coord[x]: #x가 True 인지 살펴 보는것
#         answer+=1
#         x+=L
#     else:
#         x+=1
# print(answer)



# 심화 만약 구멍의 개수가 10000000 같이 클 경우
coord = list(map(int,input().split())) # 좌표 압축 기법이라고 함

# GPT 도움 받아서 품
coord.sort()
# 이후 비슷한 로직으로 풀면 되는데 내가 한번 시도해보기
z=0 #현재 구멍을 가리키는 인덱스
while z < N:
    # 현재 구멍 위치에서 테이프를 시작으로 붙임
    start = coord[z]
    answer+=1

    #테이프가 덮는 범위 : [start, start+L)
    coverd= start+L

    #테이프 범위 안에 들어오는 구멍들은 전부 스킵
    while z < N and coord[z] < coverd:
        z += 1
print(answer)