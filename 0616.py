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

# 2. 그래프 그리기 시작
plt.figure(figsize=(12, 6))

# X축에 들어갈 임시 번호 생성 (1, 2, 3...)
x_indexes = range(1, len(category_counts) + 1)

# 막대 그래프 그리기 (hue에 index를 넣어 색상을 다르게 지정)
ax = sns.barplot(
    x=list(x_indexes),            # X축은 1, 2, 3... 숫자로 단순화
    y=category_counts.values,     # Y축은 빈도수
    hue=category_counts.index,    # ★ 핵심: 원래 글자들을 색상(hue) 기준으로 지정
    palette='Set2',               # 깔끔한 파스텔톤 색상 테마
    dodge=False                   # 막대가 겹치거나 갈라지지 않도록 설정
)

# 3. 그래프 디테일 설정
plt.title('통합 분류1 집계 (범례 구분)', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('분류 번호', fontsize=12)
plt.ylabel('데이터 개수 (건)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# 4. ★ 범례(Legend) 위치 및 스타일 조정
# 그래프 오른쪽 밖에 범례 상자를 배치합니다.
plt.legend(
    title="통합 분류1 항목", 
    bbox_to_anchor=(1.02, 1),      # 그래프 오른쪽 살짝 밖에 위치
    loc='upper left',              # 범례 상자의 왼쪽 위 기준
    borderaxespad=0.
)

plt.tight_layout()
plt.show()