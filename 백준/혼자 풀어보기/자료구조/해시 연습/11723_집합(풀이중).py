# 해시 연습
import sys
input=sys.stdin.readline
M = int(input())
s=set()
for _ in range(M):
    c,num= input().split()
    # if c=='add' and num in d:
    #     pass
    # elif c=='add' and num not in d:
    #     d[c] = num
    # if c=='remove' and num not in d:
    #     pass
    # elif c=='remove' and num in d:
    #     d[c] -= num
    # if c=='check' and num in d:
    #     1
    # elif c=='check' and num not in d:
    #     0
    # if c=='all':
    s.append(c)
    print(s)

    # 결론 -> set() 으로 푸는 문제임
    