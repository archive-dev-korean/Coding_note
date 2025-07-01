--문제 : 보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다. 보호소에 들어올 당시에는 중성화1되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59045

--복잡 & 오류1 :
 SELECT i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
 from animal_ins i join animal_outs o
 on i.animal_id = o.animal_id
 where i.SEX_UPON_INTAKE like 'Intact%' and o.SEX_UPON_OUTCOME in ('Spayed' ,'Neutered')
 order by 1

--조건에는 맞지만 원인 모르게 출력이 되지 않음(하지만 정답은 맞음)

--복잡 & 오류2 :
SELECT a.ANIMAL_ID, a.ANIMAL_TYPE, a.NAME
FROM (
   SELECT ANIMAL_ID, ANIMAL_TYPE, NAME
   FROM ANIMAL_INS
   WHERE SEX_UPON_INTAKE LIKE 'Intact%'
 ) AS a
 JOIN (
   SELECT ANIMAL_ID, ANIMAL_TYPE, NAME
   FROM ANIMAL_OUTS
   WHERE SEX_UPON_OUTCOME IN ('Spayed', 'Neutered')
 ) AS b
 ON a.ANIMAL_ID = b.ANIMAL_ID
 ORDER BY 1

--조인을 활용한 쿼리 아까보다 조금 더 복잡하고 조건 또한 만족한다. 

--가장 간단 & 정답 :
SELECT i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
FROM ANIMAL_INS i
JOIN ANIMAL_OUTS o ON i.ANIMAL_ID = o.ANIMAL_ID
WHERE i.SEX_UPON_INTAKE <> o.SEX_UPON_OUTCOME
ORDER BY i.ANIMAL_ID;

--간단하게 들어올 때 성별과 나갈 떄 성별이 다르다고 조건을 주면 주어진 문제에 만족한다. 따라서 정답
