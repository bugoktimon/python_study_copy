import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = './원본/한국언론진흥재단_뉴스빅데이터_메타데이터_노인_20011231.csv'  # 파일명을 여기에 적어주세요.


df = pd.read_csv(file_path, encoding='cp949')



# 🛠️ 통합 분류 집계 시각화


plt.rcParams["font.family"] = "Malgun Gothic"  
plt.rcParams["axes.unicode_minus"] = False  

# 1. value_counts()로 데이터 집계 (Key-Value 구조 생성)
category_counts = df['통합 분류1'].value_counts()

# 2. 시각화 (막대 그래프)
plt.figure(figsize=(10, 6))                 # 그래프 크기 조절
sns.barplot(x=category_counts.index,        # X축: Key (분류 이름)
            y=category_counts.values,       # Y축: Value (빈도수)
            palette='viridis')              # 색상 테마

# 그래프 디테일 추가
plt.title('통합 분류1 데이터 빈도수 집계', fontsize=16, fontweight='bold')
plt.xlabel('분류 항목', fontsize=12)
plt.ylabel('데이터 개수 (건)', fontsize=12)
plt.xticks(rotation=45)                     # 항목 이름이 길면 비스듬히 회전
plt.grid(axis='y', linestyle='--', alpha=0.7) # 가로 점선 추가

plt.tight_layout()                          # 여백 자동 조정
plt.show()



