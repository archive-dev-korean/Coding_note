--문제 : '경제' 카테고리에 속하는 도서들의 도서 ID(BOOK_ID), 저자명(AUTHOR_NAME), 출판일(PUBLISHED_DATE) 리스트를 출력하는 SQL문을 작성해주세요.
--결과는 출판일을 기준으로 오름차순 정렬해주세요.

--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/144854


SELECT b.BOOK_ID, a.AUTHOR_NAME, date_format(b.PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from BOOK b
join AUTHOR a on b.author_id = a.author_id
where b.category like '%경제%'
order by 3 asc

--날짜 포맷 맞춰야 해서 date_foramt 사용
