--문제: BOOK 테이블에서 2021년에 출판된 '인문' 카테고리에 속하는 도서 리스트를 찾아서 도서 ID(BOOK_ID), 출판일 (PUBLISHED_DATE)을 출력하는 SQL문을 작성해주세요. 결과는 출판일을 기준으로 오름차순 정렬해주세요.
--출처: https://school.programmers.co.kr/learn/courses/30/lessons/144853

-- Date 타입으로 되어있는 PUBLISHED_DATE에서 날짜를 연,월,일 형식으로 바꾸고 조건에 맞는 결과 출력
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE,'%Y-%m-%d') as PUBLISHED_DATE
from BOOK 
where category = '인문' and PUBLISHED_DATE LIKE '2021%'
order by PUBLISHED_DATE asc;


SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
WHERE CATEGORY = '인문' AND PUBLISHED_DATE between '2021-01-01' and '2021-12-31'
ORDER BY PUBLISHED_DATE;

-- 두번째로 적는게 조금 더 좋을 듯

