# 자료구조 연습
# stk=[]
# istack=True
# while True:  # 이렇게 하면 한문자씩 비교하는게 아니라 한 문장씩 비교해서 값이 달라짐
#     ch=input()
#     if ch == '(':
#         stk.append(ch)
#     elif ch==')':
#         if stk:
#             stk.pop()
#         else:
#             istack=False
#             break
#     elif ch=='[':
#         stk.append(ch)
#     elif ch==']':   
#         if stk:
#             stk.pop()
#         else:
#             istack=False
#             break
#     elif ch=='.':
#         break
#     if stk:
#         print('NO')
#     else:
#         print('YES')
# print(ch)
# 올바르고 균형잡힌 풀이
while True:
    line=input()
    if line =='.':
        break
    stk=[]
    istack=True
    # isstack=True
    for ch in line:
        if ch=='(' or ch=='[':
            stk.append(ch)
        elif ch==')':
            if not stk or stk[-1] != '(':
                istack=False
                break
            stk.pop()
        elif ch ==']':
            if not stk or stk[-1] != '[':
                istack=False
                break
            stk.pop()
    if istack and not stk: # isstack이 True이거나 stk가 값이 있지 않을때(값이 없을 떄)
        print('yes')
    else:
        print('no')
    # stk와 istack을 전역 변수로 두면 틀림