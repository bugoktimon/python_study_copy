import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = './원본/한국언론진흥재단_뉴스빅데이터_메타데이터_노인_20011231.csv'  # 파일명을 여기에 적어주세요.


df = pd.read_csv(file_path, encoding='cp949')



# 🛠️ 통합 분류 집계 시각화


plt.rcParams["font.family"] = "Malgun Gothic"  
plt.rcParams["axes.unicode_minus"] = False  

# 1. '통합 분류1'에서 '-' 앞자리만 추출해서 새로운 열(대분류) 만들기
# .str.strip()을 추가해 혹시 모를 앞뒤 공백까지 깔끔하게 제거합니다.
df['대분류'] = df['통합 분류1'].str.split('-').str[0].str.strip()

# 2. 앞자리만 딴 데이터로 빈도수 집계 (Key-Value 생성)
category_counts = df['대분류'].value_counts()

# 3. 그래프 그리기 시작
plt.figure(figsize=(12, 6))

# X축에 들어갈 임시 번호 생성 (1, 2, 3...)
x_indexes = range(1, len(category_counts) + 1)

# 막대 그래프 그리기 (hue에 대분류 이름을 넣어 색상 구분)
ax = sns.barplot(
    x=list(x_indexes),            # X축은 1, 2, 3... 숫자로 단순화
    y=category_counts.values,     # Y축은 집계된 개수
    hue=category_counts.index,    # 앞자리 분류명별로 색상 지정
    palette='Set2',               # 깔끔한 색상 테마
    dodge=False                   # 막대 정렬 유지
)

# 4. 그래프 디테일 설정
plt.title('통합 분류 앞자리 기준 집계 시각화', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('분류 번호', fontsize=12)
plt.ylabel('데이터 개수 (건)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# 5. 오른쪽 바깥 영역에 범례 배치
plt.legend(
    title="통합 분류 (앞자리)", 
    bbox_to_anchor=(1.02, 1),      # 그래프 오른쪽 살짝 바깥 위치
    loc='upper left',              # 범례 상자의 왼쪽 위 기준
    borderaxespad=0.
)

plt.tight_layout()
plt.show()