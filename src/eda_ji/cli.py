from president_speech.db.parquet_interpreter import get_parquet_full_path
import pandas as pd
import typer

def group_by_count(keyword, str):
    data_path = get_parquet_full_path()
    df = pd.read_parquet(data_path)
    fdf = df[df['speech_text'].str.contains(keyword, regex=False)] # 입력한 단어가 들어간 연설 df 만들
    gdf = fdf.groupby("president").size().reset_index(name="count")  # 대통령별 개수 세서 그룹화 하기
    sdf = gdf.sort_values(by='count', ascending=False).reset_index(drop=True)  # 내림차순 정렬 하기
    print(sdf.to_string(index=False))

def entry_point():
    typer.run(group_by_count)
