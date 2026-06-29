branch 이름이 잘못됨. worldcloud가 아니라 wordcloud임.
--------------------------------------------------------------
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
