# 구현 연습
# 딕셔너리로 푸는 것 같은데 key=value 받아서
N=input()
cnt=0
alpha=['c=','c-','dz=','d-','lj','nj','s=','z=']
# 각 문자열을 순회 하면서 구하려고 했던 건데 이렇게 하면 안되고
# for i in N:
#     for j in range(len(i)):
#         if i[j] and i[j-1] in alpha:
#             cnt+=1
#         else:

# while 문 써서 하는게 더 효율적
i=0
while i < len(N):
    if N[i:i+3] == 'dz=':
        cnt+=1
        i+=3
    elif N[i:i+2] in alpha:
        cnt += 1
        i += 2 
    else:
        cnt += 1
        i += 1
print(cnt)

# 정말 생각을 많이 한다면 replace로 치환하는 방법도 있음
# for a in alpha:
#     N = N.replace(a,'*')
# print(len(N))
# 어짜피 개수만 세면 되니까 해당하는 알파멧만 len() -> 1 의 값으로만 바꾸면 세는덴 문제 없음