# # 구현 연습
K,S,N=map(str,input().split())
# arr=[[0]*8 for _ in range(8)]
# print(arr)
# xk=(0,0)#킹의 초기 좌표(임의로 둠)
# xs=(0,0) #돌의 초기 좌표(임의로 둠)
# # dxr,dyr
# R=[0,1]
# # dxl,dyl
# L=[0,-1]
# # dxb,dyb
# B=[1,0]
# # dxT,dyt
# T=[0,1]
# # dxrt,dyry
# RT=[1,-1]
# # dxlt,dylt
# LT=[-1,-1]
# # dxrb,dyrb
# RB=[1,1]
# # dxlb,dylb
# LB=[-1,1]

# for _ in range(int(N)):
#     i=input()
#     if i==B:
#         xk+=B
#     elif i==L:
#         xk+=L
#     elif i==R:
#         xk+=R
#     elif i==T:
#         xk+=T
#     elif i==RT:
#         xk+=RT
#     elif i==LT:
#         xk+=LT
#     elif i==RB:
#         xk+=RB
#     else:
#         xk+=LB

# 킹과 돌의 초기 좌표
xk=int(K[1]) - 1
yk=ord(K[0]) - ord('A')
# print(xk,yk)
xs=int(S[1]) - 1
ys=ord(S[0]) - ord('A')

#방향
move = {
    "R": (0,1),
    "L": (0,-1),
    "B": (-1,0),
    "T": (1,0),
    "RT": (1,1),
    "LT": (1,-1),
    "RB": (-1,1),
    "LB": (-1,-1)
}
def inside(x,y):
    return 0 <= x <8 and 0 <= y < 8

for _ in range(int(N)):
    i=input()
    # for i in move.keys():
    #     if i =='R':
    #         arr[xk][yk]+=move[i]
    #     elif i=='L':
    #         arr[xk][yk] +=move[i]
    #     elif i=='B':
    #         arr[xk][yk] +=move[i]
    #     elif i=='T':
    #         arr[xk][yk] +=move[i]
    #     elif i=='RT':
    #         arr[xk][yk] +=move[i]
    #     elif i=='LT':
    #         arr[xk][yk] +=move[i]
    #     elif i=='RB':
    #         arr[xk][yk] +=move[i]
    #     else:
    #         arr[xk][yk] +=move[i]
    dx,dy = move[i]
    # xk += dx
    # yk += dy
    
    # 좌표값 변수 -> 경계 판단할 때 사용
    nxk,nyk = xk + dx, yk + dy
    if not inside(nxk,nyk):
        continue # 킹이 밖이면 무시

    # 킹이 돌로 이동하면 -> 돌도 같은 방향으로 이동
    if nxk == xs and nyk == ys:
        nxs,nys = xs + dx, ys+dy
        if not inside(nxs,nys):
            continue
        xs, ys = nxs, nys # 돌 이동
    xk,yk = nxk,nyk # 킹 이동
print(chr(yk + ord('A'))+str(xk+1))
print(chr(ys + ord('A'))+str(xs+1))