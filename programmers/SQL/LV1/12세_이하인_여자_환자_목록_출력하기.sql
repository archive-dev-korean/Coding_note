--문제: PATIENT 테이블에서 12세 이하인 여자환자의 환자이름, 환자번호, 성별코드, 나이, 전화번호를 조회하는 SQL문을 작성해주세요. 이때 전화번호가 없는 경우, 'NONE'으로 출력시켜 주시고 결과는 나이를 기준으로 내림차순 정렬하고, 나이 같다면 환자이름을 기준으로 오름차순 정렬해주세요.
--출처: https://school.programmers.co.kr/learn/courses/30/lessons/132201

--ifnull을 사용해 문제 조건에 맞게 NULL값을 수정후에 조건에 맞는 결과값 출력
SELECT PT_NAME, PT_NO, GEND_CD, AGE, ifnull(tlno, 'NONE') AS TLNO
FROM PATIENT 
WHERE AGE <= '12' AND GEND_CD ='W'
order by age desc, pt_name asc
