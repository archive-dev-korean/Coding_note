# 문제 : 어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.

def solution(n, t):
    return n * (2 ** t)
  # 이렇게 써야 하는데 문제 풀 당시 좀 생각이 많았는지 제곱이 된다는 걸 몰랐다

def solution(n, t):
    for _ in range(t):
        n *= 2
    return n

# 몰랐을 땐 이렇게 풀면 되긴 한다.
