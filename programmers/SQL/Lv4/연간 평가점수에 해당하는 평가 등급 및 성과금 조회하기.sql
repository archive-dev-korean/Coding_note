--문제 : HR_DEPARTMENT, HR_EMPLOYEES, HR_GRADE 테이블을 이용해 사원별 성과금 정보를 조회하려합니다. 평가 점수별 등급과 등급에 따른 성과금 정보가 아래와 같을 때, 사번, 성명, 평가 등급, 성과금을 조회하는 SQL문을 작성해주세요.

-- 평가등급의 컬럼명은 GRADE로, 성과금의 컬럼명은 BONUS로 해주세요.
-- 결과는 사번 기준으로 오름차순 정렬해주세요


--정답 (서브 쿼리 활용)
select e.EMP_NO, e.EMP_NAME, case
when a.score >= 96 then 'S'
when a.score >= 90 then 'A'
when a.score >= 80 then 'B'
else 'C'
end as GRADE, 
case
when a.score >= 96 then e.SAL * 0.2
when a.score >= 90 then e.SAL * 0.15
when a.score >= 80 then e.SAL * 0.1
else e.SAL * 0
end as BONUS
from HR_EMPLOYEES e 
join
(select EMP_NO, avg(SCORE) as score
from HR_GRADE
group by 1
) a on e.EMP_NO = a.EMP_NO
order by 1

--처음에 성과급을 월급에 더해서 총 sal을 구했는데 그게 틀린 것 같다. 1,1 이런식으로 구했었다.

