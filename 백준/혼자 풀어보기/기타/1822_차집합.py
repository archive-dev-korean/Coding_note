# set연습
import sys
input=sys.stdin.readline
A,B=map(int,input().split())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# result=[]
# # print(len(a-b)
# for i in a:
#     if i not in b:
#         result.append(i)
# print(len(result))
# for j in result:
#     print(j,end=' ')
## 리스트로 풀면 시간 초과 나니까
a=set(map(int,input().split()))
b=set(map(int,input().split()))
result=set()
result=a-b
print(len(result))
for i in sorted(result):
    print(i,end=' ')
