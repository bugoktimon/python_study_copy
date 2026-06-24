import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file_path = './원본/한국언론진흥재단_뉴스빅데이터_메타데이터_노인_20011231.csv' 
df = pd.read_csv(file_path, encoding='cp949')


region_mask = df["통합 분류1"].notna() & df["통합 분류1"].str.contains("지역") # notna 빈값 빼내라. 통합분류1에서 지역이 들어있는 데이터와 비어있지 않은 것들만 region_mask로 옮겨
# 지역기사만 추출해라
df_region = df[region_mask].copy()


df_region['상세지역'] = df_region['통합 분류1'].apply(  # 상세지역이라는 새로운 칼럼을 만듬
    lambda x: x.split('-')[-1].strip() if '-' in str(x) else x.strip()  # 그 x를 - 기준으로 분할하고.(-1이면 역행. 제일 마지막 -을 뜯어내라). strip 공백이있으면 제거해라. 그리고 상세지역에 주라. else 하이픈이 없는 경우 공백만빼고 보내줘.
)
# 1회용 함수 람다
# lambda x: [조건이 참일 때 매수] if [조건식] else [조건이 거짓일 때 매수]

print("=== [콘솔 확인] 1. 추출된 상세지역 상위 빈도수 ===")
print(df_region['상세지역'].value_counts(),  # 충남 충남 충남 개수 포개둔 것. 충남 몇개 나왔는지 value_count() 이렇게 나온 결과물을 시리즈. (키, 밸류 딕셔너리와 비슷)
      f"\n 상세지역은 총 {len(df_region['상세지역'].value_counts())}개")
print("====================================================\n")


df_region['키워드'] = df_region['키워드'].fillna('') # 결측치 만들고싶지 않아서 fillna.
# 빈문자열이라도 삽입 


from collections import Counter
# 어떤 요소가 몇 개씩 들어있는지 계산하여 딕셔너리 형태로 반환

# 키워드컬럼에서 키워드 순위 10
def get_top_10_keywords(series): # 매개인자 series
   
    all_text = " ".join(series.astype(str))  # series 타입을 문자로 만들겠다. 하나의 문자열로 쭉 길게 만듬.
    words = [word.strip() for word in all_text.replace(',', ' ').split() if word.strip()]  # word.strip() 공백을 없앨 것이다. 쉼표가 있으면 공백으로 처리하고 한개씩 분리시켜서 몇개인지 계산하고자함.
    
  
    top_10 = [item[0] for item in Counter(words).most_common(10)] # words를 세서 10개만 top 10으로 넘겨
    
    return top_10


summary_df = df_region.groupby('상세지역').agg( # 뉴스빈도수와 키워드순 합쳐서 만드는게 agg임
    뉴스빈도수=('상세지역', 'count'),
    키워드순=('키워드', get_top_10_keywords)
).sort_values(by='뉴스빈도수', ascending=False)


"""
print("=== [콘솔 확인] 4. 상세지역별 통합 키워드 순위  ===")
print(summary_df)
print("\n----------------------------------------------------")
print("데이터프레임 정보 및 타입 확인:")
print(summary_df.info())
print("====================================================\n")
"""

stopwords = {
    '노인', '노인들',
    '지역', '주민',
    '사회', 
    '사업', '행사',
    '전달', 
    '지원', '추진',
    '시설', '운영',
    '회장', '참석',
    '활동',
    '사랑'
}

# 지역명도 제거
regions = set(df_region['상세지역'].unique())
stopwords.update(regions)

print(stopwords)

