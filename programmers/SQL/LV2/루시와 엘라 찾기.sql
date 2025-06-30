-- 문제 : 동물 보호소에 들어온 동물 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디와 이름, 성별 및 중성화 여부를 조회하는 SQL 문을 작성해주세요.
-- 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59046

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
from ANIMAL_INS 
where NAME in ('Lucy', 'Ella', 'Pickle', 'Rogan','Sabrina','Mitty')
-- in 절에서 튜플로 이루어진 값만 아니라면 or 연산 
