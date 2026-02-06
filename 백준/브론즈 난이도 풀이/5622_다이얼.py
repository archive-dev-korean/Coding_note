# 연습
A=input().upper()
result=0
d=dict()
for i in range(1,12):
    if i <= 9:    
        d[i] = i+1
    else:
        d[0] = 11
# print(d)
for i in A:
    if i=='A' or i=='B' or i=='C':
        i=2
    elif i=='D' or i=='E' or i=='F':
        i=3
    elif i=='G' or i=='H'or i=='I':
        i=4
    elif i=='J' or i=='K' or i=='L':
        i=5
    elif i=='M'or i=='N' or i=='O':
        i=6
    elif i=='P' or i=='Q' or i=='R' or i=='S':
        i=7
    elif i=='T' or i=='U' or i=='V':
        i=8
    # elif i=='W' or i=='X' or i=='Y' or i=='Z':
    #     i=9
    else:
        i=9
    result+=d[i]
print(result)

# 더 간단히
for ch in A:
    if ch in "ABC":
        result += 3
    elif ch in "DEF":
        result += 4
    elif ch in "GHI":
        result += 5
    elif ch in "JKL":
        result += 6
    elif ch in "MNO":
        result += 7
    elif ch in "PQRS":
        result += 8
    elif ch in "TUV":
        result += 9
    else:  # WXYZ
        result += 10

print(result)