"""
=========================================
설정 파일화(Configuration) 또는 하드코딩 제거(De-hardcoding)
추상화 1단계 (Abstraction)
[시각화 관점] 딕셔너리 기반 설정 통합화 작업 (1차)
- 함수 미사용, 값 수정의 편의성 확보 목적
=========================================
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ----------------------------------------------------
# [★ 설정 통합화 딕셔너리] 이 부분의 값만 수정하면 됩니다.
# ----------------------------------------------------

config = {
    # 데이터 설정
    "file_path": "./원본/한국언론진흥재단_뉴스빅데이터_메타데이터_노인_20011231.csv",
    "target_column": "일자",  # 분석하고자 하는 특정 컬럼
    "top_n": 10,  # 노출할 상위 순위 개수
    # 스타일 및 디자인 설정
    "font_family": "Malgun Gothic",  # Mac은 'AppleGothic'
    "palette": "Set3",  # 그래프 색상 팔레트
    "figsize": (10, 7),  # 도화지 크기 (가로, 세로)
    # 텍스트 레이블 설정
    "title": "뉴스 일자별 발행 비중 TOP 10",
    "xlabel": "뉴스 발행 건수 (건)",
    "ylabel": "뉴스 일자 고유 색상 (우측 범례 참조)",
    "legend_title": "일자 카테고리",
}
# 1. 데이터 로드 및 전처리 (딕셔너리 값 참조)
df = pd.read_csv(config["file_path"], encoding="cp949")

# 2. 특정 컬럼의 빈도수를 계산하여 시리즈 생성 (딕셔너리 값 참조)
category_counts = (
    df[config["target_column"]].value_counts().head(config["top_n"])
)

# 3. ★반드시 콘솔에 시리즈 구조와 데이터 확인
print(f"=== [콘솔 확인] {config['target_column']} 카테고리 시리즈 ===")
print(category_counts)
print("데이터 타입:", type(category_counts))
print("====================================================\n")

# 4. 한글 폰트 및 그래프 기본 설정
plt.rcParams["font.family"] = config["font_family"]
plt.rcParams["axes.unicode_minus"] = False

# 5. 그래프 크기 설정
plt.figure(figsize=config["figsize"])

# 6. 가로 막대 차트 생성 (딕셔너리 기반 동적 할당)
ax = sns.barplot(
    x=category_counts.values,
    y=category_counts.index,
    hue=category_counts.index,
    palette=config["palette"],
    legend=True,
)

# 7. 축 레이블 및 스타일 설정
ax.set_yticklabels([])  # Y축 텍스트 숨김 (범례 대체)
plt.xlabel(config["xlabel"], fontsize=12, labelpad=10)
plt.ylabel(config["ylabel"], fontsize=12, labelpad=10)
plt.title(config["title"], fontsize=16, fontweight="bold", pad=20)

# 8. 가로 막대 우측 끝에 데이터 값 표시
for i, value in enumerate(category_counts.values):
    plt.text(value + 0.1, i, f" {value}건", va="center", ha="left", fontsize=11)

# 9. 범례 설정 적용
plt.legend(
    title=config["legend_title"],
    loc="upper right",
    bbox_to_anchor=(1.35, 1),
    frameon=True,
    shadow=True,
)

# 10. 그래프 출력
plt.tight_layout()
plt.show()