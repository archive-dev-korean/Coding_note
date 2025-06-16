--문제: FISH_INFO 테이블에서 잡은 물고기 중 가장 큰 물고기의 길이를 'cm' 를 붙여 출력하는 SQL 문을 작성해주세요. 이 때 컬럼명은 'MAX_LENGTH' 로 지정해주세요.
--출처: https://school.programmers.co.kr/learn/courses/30/lessons/298515

--concat 연산자 사용해서 가장큰 길이와 'cm' 합침
select concat(MAX(LENGTH), 'cm') as MAX_LENGTH from FISH_INFO
