--문제 : 관리자의 실수로 일부 동물의 입양일이 잘못 입력되었습니다. 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일이 빠른 순으로 조회해야합니다.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59043

SELECT i.ANIMAL_ID, i.NAME
from ANIMAL_INS i join ANIMAL_OUTS o on i.ANIMAL_ID = o.ANIMAL_ID
where o.DATETIME < i.DATETIME and o.DATETIME is not null
order by i.DATETIME asc

-- is not null 조건은 있어도 없어도 정답에 영향을 끼치진 않는 것 같다. 하지만 확실히 하기 위해 넣음
