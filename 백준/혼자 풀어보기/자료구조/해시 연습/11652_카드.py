# 해시 연습
import sys
input = sys.stdin.readline
N = int(input())
d=dict()
for _ in range(N):
    i = int(input())
    if i in d:
        d[i] +=1
    else:
        d[i] =1
# print(d.items())
# G=list(d.items())
# G.sort(key=lambda x :x[0],reverse=True)
# G.sort(key=lambda x: x[1],reverse=True)
# for k,v in G:
#     print(k)
#     break

# 이거 틀렸음(위에)
# 고쳐보면
mx = max(d.values())
cands =[]
for k,v in d.items():
    if v==mx:
        cands.append(k)
print(min(cands))

#아래 처럼 적어도 됨
# ans = min(k for k,v in d.items() if v==mx)
# print(ans)