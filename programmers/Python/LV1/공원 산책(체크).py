# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/172928

오답(내맘대로 품) : 
def solution(park, routes):
    answer = []
    for i in park:
        for j in i:
            if j == 'S':
                p=0
                w=0
                if routes[i][0] == 'E':
                    p += 1*routes[i][2]
                elif p > len(i):
                    continue
                elif routes[i][0] == "S":
                    w += 1*rountes[i][2]
                elif w >len(i):
                    continue
                elif routes[i][0] == "W":
                    p -= 1*routes[i][2]
                elif p>len(i):
                    continue
            answer.append(p,w)
            
            else:
                continue
                
    return answer

# 이상한 로직

정답 : 
def solution(park, routes):
    H = len(park)
    W = len(park[0])

    # 1) 시작점(S) 찾기 (안전하게 한 번에 탈출)
    sr = sc = None
    for r, row in enumerate(park):
        c = row.find('S')
        if c != -1:
            sr, sc = r, c
            break
    # 혹시 S가 없을 경우 대비 (문제 조건엔 거의 없음)
    if sr is None:
        return [0, 0]

    # 2) 방향 매핑
    dmap = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}

    r, c = sr, sc

    # 3) 명령 처리 (스텝 단위 시뮬레이션 + 매 스텝 경계/장애물 체크)
    for cmd in routes:
        parts = cmd.split()
        if len(parts) != 2:
            continue  # 방어적 처리
        d, s = parts[0], int(parts[1])
        if d not in dmap:
            continue

        dr, dc = dmap[d]
        nr, nc = r, c
        ok = True
        for _ in range(s):
            nr += dr
            nc += dc
            # 경계 먼저 체크 (인덱싱 전에!)
            if not (0 <= nr < H and 0 <= nc < W):
                ok = False
                break
            if park[nr][nc] == 'X':
                ok = False
                break

        if ok:   # 명령 전체가 유효할 때만 위치 갱신
            r, c = nr, nc

    return [r, c]
# GPT 로직인데 아직도 잘 모르겠음 왜 맞는지 이거 확인 해보기
