--문제 : HR_DEPARTMENT, HR_EMPLOYEES, HR_GRADE 테이블에서 2022년도 한해 평가 점수가 가장 높은 사원 정보를 조회하려 합니다. 2022년도 평가 점수가 가장 높은 사원들의 점수, 사번, 성명, 직책, 이메일을 조회하는 SQL문을 작성해주세요.
--2022년도의 평가 점수는 상,하반기 점수의 합을 의미하고, 평가 점수를 나타내는 컬럼의 이름은 SCORE로 해주세요.

--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/284527

--오답 쿼리1 : 
# select sum(g.score) as score ,e.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
# from HR_DEPARTMENT d
# join on HR_EMPLOYEES e on e.DEPT_ID
# join on HR_GRADE g on g.EMP_NO
# where YEAR in ('2022')

-- 이러면 아예 조회가 안되고 일단 HR_DEPARTMENT이 테이블을 사용할 필요가 없는데 조인해서 사용함
--group by도 안되어 있어서 에러남,
--하나만 출력해야 하는데 이렇게 적으면 여러 값 출력 됨

--오답 2:
# select max(sum(g.score)) as score, e.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
# from HR_EMPLOYEES e, HR_GRADE g
# where e.EMP_NO = g.EMP_NO 

--일단 조회 안되는 건 똑같고, 집계함수(집계함수) 이런식으로 사용이 불가능
--group by 안써서 여러 값 출력됨


--정답:
select sum(g.score) as score, e.emp_no, e.emp_name, e.position, e.email
from HR_EMPLOYEES e
join HR_GRADE g on e.EMP_NO = g.EMP_NO
group by e.emp_no
order by score desc
limit 1

--사원 번호 별로 group by해서 점수의 총합을 구한다음 접수별로 내림차순 한 다음 그중 하나만 출력
