import pandas as pd

# CSV 파일 경로 지정

# 이것은 판다스(pandas)가 CSV 파일을 기본값인 UTF-8 방식으로 읽으려고 시도했으나, 
# 파일 안에 한글(텍스트) 인코딩 방식(주로 엑셀의 CP949)이 달라서 파일을 해석못해 발생한 대표적인 오류

# 기존 코드: df = pd.read_csv(file_path)
# 변경 코드: 뒤에 encoding='cp949'를 추가

file_path = './원본/한국언론진흥재단_뉴스빅데이터_메타데이터_노인_20011231.csv'  # 파일명을 여기에 적어주세요.

# CSV 파일을 읽어서 데이터프레임으로 변환
df = pd.read_csv(file_path, encoding='cp949')

# 상위 5개 데이터 확인
# print(df.head())

df.info()