# 해시 연습
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
# s=set()
d=dict()
for _ in range(N):
    i=input().rstrip()
    if i in d:
        d[i] += 1
    else:
        d[i] =1
# print(d)
# 여기서부터 정렬 조건 추가해 봄 -> 리스트로 변환 해야함 딕셔너리는 정렬 못 해서 리스트로 변환 해야함
G=list(d.items())
G.sort(key=lambda x:x[0]) #사전순 오름차순
G.sort(key=lambda x:len(x[0]), reverse=True) # 단어 길이 내림차순
G.sort(key=lambda x: x[1], reverse=True) # 빈도 내림차순

# 빈도, 단어길이, 사전순 순서로 쓰면 틀림(쓴 순서와 반대로 정렬됨)

out=[]
for k,v in G:
    # print(k,v)
    if len(k) >= M:
        # print(k)
        out.append(k)

sys.stdout.write("\n".join(out))

# 이거는 입/출력 형식이 sys 쓰는 거라 백준에서만 해당하는 사항 같아서 따로 메모는 안할 것
# stdin.readline 이렇게 쓰면 단어 끝에 \n이 같이 들어옴
# 그개서 print() 로 찍으면 올바르지 않은 형식으로 출력됨.