# 구현 연습
m=['a','e','i','o','u']
while 1:
    s=input()
    if s=='end':
        break
    # 여기서 변수 추가
    acceptable = True
    has_vowel = False
    vowel_cnt=0
    cons_cnt=0

    for i in range(len(s)): 
        if s[i] in m: # 모음 포함 여부 검사
            has_vowel = True
            vowel_cnt +=1
            cons_cnt =0
        else:
            cons_cnt+=1
            vowel_cnt=0
        if vowel_cnt==3 or cons_cnt==3: # 모음/자음 3연속
            acceptable=False
            break
        if i> 0 and s[i] == s[i-1]: # 같은 문자 연속(ee,oo제외)
            if s[i] not in ['e','o']:
                acceptable=False
                break
    if not has_vowel: #모음 최소 1개
        acceptable = False
    if acceptable:
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")
    # for i,v in enumerate(s):
    #     print(i)
    #     if v in m and s[i-2] != s[i-1] and s[i-1] != s[i]:
    #         print('<' + s +'>', 'is acceptable.')
    #     else:
    #         print('<'+s+'>', 'is not acceptable')