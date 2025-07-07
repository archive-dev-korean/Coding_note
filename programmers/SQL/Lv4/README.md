# 계층쿼리 
- MySQL인 경우 : 재귀 CTE -> with recursive 테이블명 as 이런 형태로 사용함. 루트노드와 자식노드를 직접 지정해 줘야함. 부모 자식간 연결도 join을 사용해 직접 연결 해 줘야함.
  - 루트 노드 지정할 경우 where 루트값 is null 이런 방식으로 지정
- oracle일 경우 : connect by 로 사용해서 루트 노드를 start with로 지정해서 간단하게 사용가능.
