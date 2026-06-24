import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file_path = './원본/한국언론진흥재단_뉴스빅데이터_메타데이터_노인_20011231.csv' 
df = pd.read_csv(file_path, encoding='cp949')


region_mask = df["통합 분류1"].notna() & df["통합 분류1"].str.contains("지역") # notna 빈값 빼내라. 통합분류1에서 지역이 들어있는 데이터와 비어있지 않은 것들만 region_mask로 옮겨. 행단위로 빼겠다. 
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



print("=== [콘솔 확인] 4. 상세지역별 통합 키워드 순위  ===")
print(summary_df)
print("\n----------------------------------------------------")
print("데이터프레임 정보 및 타입 확인:")
print(summary_df.info())
print("====================================================\n")


keyword_series = summary_df['키워드순']
print("=== [콘솔 확인] 5. '키워드순' 컬럼 (시리즈 구조) ===")
print(keyword_series.head(10))
print(f"데이터 타입: {type(keyword_series)}")
print("====================================================\n")


# 분석에 무의미한 불용어(Stopwords)를 걸러내는 작업

# 제외 키워드(불용어) 리스트 정의
# --------------------------------------------------
# 기본적으로 제외할 단어들을 세트(Set) 구조로 등록합니다. (검색 속도 최적화)
base_stop_words = {'노인', '참석', '일동', '주민', 
                   "지역", "마을", "노인들", "노인분들", "주민들","주민일동",
                   "이날" }
all_region_names = list(df_region['상세지역'].dropna().unique())

def get_clean_keywords(text): # 문자열을 받아서 배열을 돌려준다.
    if not text: return [] 
    words = [word.strip() for word in str(text).replace(',', ' ').split() if word.strip()] # 공백을 제거하다 strip.글자 하나하나를 공백을 제거하면서 word.strip()에 넣는것. 쉼표가 있으면 뜯어서 넘겨주라.
    
    clean_words = []
    for word in words:
        if word in base_stop_words: continue # 내가 넣은 글자가 base stop words 속에 있으면 continue 건너뛰고 중단하고 다시 for 로 돌아가. 
        if any(region in word for region in all_region_names): continue
        clean_words.append(word)
    return clean_words

# --------------------------------------------------
# 3. 상세지역별 키워드 통합 및 상위 5개 추출 (키워드순 컬럼 생성)
# --------------------------------------------------
df_region['정제된_리스트'] = df_region['키워드'].apply(get_clean_keywords) # 행단위로 빼겠다. 지역만 속아낸 데이터프레임 중 키워드 시리즈를 get_clean_keywords로 적용해라. 데이터프레임에 정제된 리스트 컬럼이 늘어난 상태.

def merge_and_rank(series): # 키밸류 키밸류 => 시리즈 (컬럼1개 잘라오는 것) 
    merged_list = [word for sublist in series for word in sublist]
    return [item[0] for item in Counter(merged_list).most_common(10)] # 중복안일어나게 counter 세고, 위에서 10위권 애들만 배열화 시켜서 내보내기. 내림차순

summary_df = df_region.groupby('상세지역').agg(
    키워드순=('정제된_리스트', merge_and_rank)
)

# 최종 출력용 시리즈 구조 생성
category_counts = summary_df['키워드순']

# --------------------------------------------------
# [콘솔 확인] 기존 출력 포맷 유지
# --------------------------------------------------
print("=== [콘솔 확인] 통합 분류1 카테고리 시리즈 ===")
print(category_counts)
print("데이터 타입:", type(category_counts))
print("====================================================\n")



