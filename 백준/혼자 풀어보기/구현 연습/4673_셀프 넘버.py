# 구현 연습
def d(n):
    s = n
    while n:
        s += n % 10
        n //= 10
    return s
generated = [False] * 10001

for n in range(1,10001):
    g = d(n)
    if g <= 10000:
        generated[g] = True
for i in range(1,10001):
    if not generated[i]:
        print(i)


#이거 어려움() False배열 만들어서 체크 해야 되기 때문에 구현, 생각하는 것 모두 잘 안 떠오를 수 있음.