# 그리디 연습
N=int(input())
D=list(map(int,input().split())) # 거리
P=list(map(int,input().split())) # 가격
# print(N,D,P)
# result=[]
# mp=max(P)
# minp=min(P)
# for i in range(len(D)):
#    if mp==P[0]:
#       result.append(P[0]*D[0])
#       print(result)
#    elif minp==P[0]:
#         result.append(P[0]*sum(D))
#         print(result)
#    else:
#        result.append(D[i]*P[i])
# print(min(result))
min_price=P[0]
cost=0
for i in range(N-1):
    min_price=min(min_price,P[i]) #이게 개빡세네
    cost+=min_price*D[i] # 여기랑 
print(cost)

# 문제에 한 번 산 기름은 다음 도시까지 들고 갈 수 있음 이렇게 해석 가능함
# 즉 도시마다 꼭 주유할 필요 없음
# 와 근데 이거 생각하는거 어렵네
