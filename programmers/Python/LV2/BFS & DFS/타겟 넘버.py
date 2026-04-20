
# def solution(numbers, target):
#     answer = 0
#     edges=[]
#     adj=[[]  for _ in range(len(numbers))]
#     for i in range(len(numbers)):
#         for j in range(i+1,len(numbers+1)):
#             edges.append([numbers(i),numbers(j)])
#     for u,v in edges:
#         adj[u].append(v)
#     def dfs(now):
#         for nxt in range(1,n+1):
#             if adj[now][nxt]==1:
#     return answer
# 이렇게 백준에서 하던 방식대로 트리 구성해서 풀려고 시도 했는데 이 접근법 자체가 틀렸음

# 이렇게 재귀 방식을 써서 풀어야 풀리는데 이해하기가 좀 어려웠음
# 일단 트리구조는 직접 만들어서 푸는 것이 아니고
# 재귀 방식으로 트리 구조가 자동으로 만들어짐 
    #             0
    #          /     \
    #       +1          -1
    #      /   \        /   \
    #  +1      -1   +1      -1

# 이렇게 가는건데 원리는
# 이걸 조금 더 직관적으로 보면
# (0,0)
# ├─ (1,1)
# │  ├─ (2,3)
# │  │  ├─ (3,6)
# │  │  └─ (3,0)
# │  └─ (2,-1)
# │     ├─ (3,2)
# │     └─ (3,-4)
# └─ (1,-1)
#    ├─ (2,1)
#    │  ├─ (3,4)
#    │  └─ (3,-2)
#    └─ (2,-3)
#       ├─ (3,0)
#       └─ (3,-6)

# 이런식으로 구성이 됨 이걸 함수에서 주석 처리한 printf부분을 찍어버 봐보면
# 어떤 방식으로 돌아가는 지 볼 수 있음


def solution(numbers,target):
    answer=0
    n=len(numbers)
    
    def dfs(idx,total):
        nonlocal answer
        # print(f"호출: dfs({idx},{total})")
        
        if idx == n:
            if total == target:
                answer+=1
                # print(f" 성공! total={total}")
            # else:
                # print(f"실패! total={total}")
            return 
        dfs(idx +1, total + numbers[idx])
        dfs(idx +1, total - numbers[idx])
    dfs(0,0)
    return answer