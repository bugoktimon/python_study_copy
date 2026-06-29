branch 이름이 잘못됨. worldcloud가 아니라 wordcloud임.
----------------------------------------------------------------------------------------------------------------------------
깃에 업로드 하는 명령어

git commit -a "워드클라우드 및 한글폰트주의(영문이름)"
fatal: paths '워드클라우드 및 한글폰트주의(영문이름) ...' with -a does not make sense => git add 를 하고 commit 메시지도 함께 하는 명령어인데 이게 안돼서 결국 따로 

git reset d#########$$$$##3##a###########################
Unstaged changes after reset:
D       Set타입.py
D       find.py
D       for.py
D       test.py
D       문자열을리스트로.py
D       설명.txt
D       시각화사용성.py
D       제너레이터표현식.py
D       지역별핵심키워드3위시각화.py
D       지역별핵심키워드개별시각화.py
D       텍스트마이닝.py
M       특정컬럼확인하기.py

git add .

git commit -m "워드클라우드 및 한글폰트주의(영문이름)" 

git push origin worldcloud 


----------------------------------------------------------------------------------------------------------------------------
graph 에서 우클릭 copy commit hash dc#################################

git reset dc#################################
Unstaged changes after reset:
M       지역별핵심키워드3위시각화.py

git add .

git commit -m "시리즈연산자 및 데이터프레임 시각화"

git push origin dimension3

git push origin dimension3 --force 

(위에서 수정한 내역과 아래서 수정한 내역이 충돌이나서 아래(과거에) 수정한 내역을 취소하고 합쳐서 같이 강제로 올려버림. 
