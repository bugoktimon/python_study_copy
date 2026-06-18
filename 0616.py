import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = './원본/한국언론진흥재단_뉴스빅데이터_메타데이터_노인_20011231.csv'  # 파일명을 여기에 적어주세요.


df = pd.read_csv(file_path, encoding='cp949')



# 🛠️ 통합 분류 집계 시각화


plt.rcParams["font.family"] = "Malgun Gothic"  
plt.rcParams["axes.unicode_minus"] = False  


##### 여기서 부터 커스터마이징 #####

'''
LLM 프롬프트 명령어

1. 주제 : **주요 언론사별 뉴스 발행량 비교**
    주력컬럼 : 언론사, 일자
    시각화 메서드 : 막대 차트 (Bar Chart)
    X축 : 언론사
    Y축 : 뉴스 발행 건수

    이거 주제로 df가 전체 데이터프레임이야
    시각화를 위한 시리즈를 생성해줘
    반드시 시리즈를 콘솔에 확인시켜줘야해 그 다음에 시각화진행 

'''

