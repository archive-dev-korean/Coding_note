# 구현 연습
# 패턴을 찾는 문제 인데 GPT 에게 물어보니
# 1번째 : 1/1 -> 합2
# 2번 째 : 1/2 , 2/1 -> 각각 합 3
# 3번째 : 3/1, 2/2, 1/3 -> 각각 합 4
# 4번 째 : 1/4, 2/3, 3/2, 4/1 -> 각각 합 5
# ...
# 패턴이 보임?

# 짝수 대각선 : 분자 1 -> k, 분모 k ->1
# 훌수 대각선 : 분자 k -> 1, 분모 1 ->K

# x가 몇 번쨰 대각선인지 찾고
# 그 대각선 안에서 몇 번쨰인지(pos) 구하고
# k가 짝수 이면 pos/(k-pos+1), 홀수면 (k-pos+1)/Pos

#구현하면
X=int(input())
k=1
total=1

while X > total:
    k+=1
    total +=k
pos = X - (total -k)

if k% 2 ==0:
    num = pos
    den = k - pos +1
else:
    num = k -pos + 1
    den = pos
print(f"{num}/{den}")