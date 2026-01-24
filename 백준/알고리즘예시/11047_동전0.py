# 전형적으로 Greedy 알고리즘으로 푸는 문제
# 왜나면 각 원소들이 규칙성이 있음(배수) -> 이런 경우는 보통 그리디 쓴다고 함

N, K = map(int,input().split())
c = []
for _ in range(N):
    c.append(int(input()))
# print(c)
c.reverse() #제일 큰 단위가 첫번째로 됨
answer = 0
for i in c:
    answer += K // i # 전체 수를 나눈 몫
    K %= i #나누고 나머지 저장 
# 루프 돌아서 판단
# 검증
    # print(f"coin:{i},k:{K}, ans:{answer}")
print(answer)