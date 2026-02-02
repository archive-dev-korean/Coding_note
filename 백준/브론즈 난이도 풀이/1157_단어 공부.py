# 연습
import sys
input=sys.stdin.readline
N=input().upper().strip()
d=dict()
for i in N:
    if i in d:
        d[i] +=1
    else:
        d[i] =1
mv=max(d.values())
# found=False
# cnt=''
# for k, v in d.items():
#     if v==mv:
#         if found: #True면
#             print("?")
#             break
#         found= True
#         cnt=k
# else:
#     print(cnt)
        # cnt+=1
        # if cnt>=2:
        #     print("?")
        #     break
        # else:
        #     print(k)

result=[]
for k,v in d.items():
    if v == mv:
        result.append(k)
if len(result) >=2:
    print('?')
else:
    print(result[0])
    