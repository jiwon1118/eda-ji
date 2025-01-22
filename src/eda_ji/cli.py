from president_speech.db.parquet_interpreter import get_parquet_full_path
import pandas as pd
import typer

def group_by_count(keyword: str, ascen: bool=False, n: int=12) -> pd.DataFrame:
    data_path = get_parquet_full_path() # 데이터 경로 가져오기 
    df = pd.read_parquet(data_path)  # 데이터 프레임으로 로드
    fdf = df[df['speech_text'].str.contains(keyword, case=False)] # 키워드가 들어간 연설 필터링 
    gdf = fdf.groupby("president").size().reset_index(name="count")  # 대통령별 그룹화 하고 개수 세기 
    sdf = gdf.sort_values(by='count', ascending=ascen).reset_index(drop=True)  # 정렬
    rdf = sdf.head(n)
    print(rdf)
    return rdf

# 추가 요청사항
# 검색 단어가 등장하는 ROW 에 speech_text 속에 해당 단어가 나오는 횟수를 모두 count 하여 그 총합을 대통령별로 다시 sum

def entry_point():
    typer.run(group_by_count)
