#해시 연습
A, B = map(int,input().split())
num_a = map(int,input().split())
num_b = map(int,input().split())

sa = set()
sb = set()
sa.update(num_a)
# print(sa)
sb.update(num_b)
# print(sb)
minus1 = sa - sb 
# print(minus1)
minus2 = sb - sa
# print(minus2)

print(len(minus1 | minus2))
