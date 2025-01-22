from eda_ji.cli import group_by_count
import pandas as pd

def test_search():
    row_count = 13
    # When
    df = group_by_count(keyword="자유", ascen=True, n=row_count)
    # assert
    assert isinstance(df, pd.DataFrame) 
    assert len(df) < row_count

def test_정렬 및 행수제한_noascen():
    row_count = 3
    is_asc = True
    # When
    df = group_by_count(keyword="자유", ascen=is_asc, n=row_count)
    # assert
    assert isinstance(df, pd.DataFrame)
    assert df.iloc[0]["president"] == "윤보선"
    assert len(df) == row_count

def test_정렬 및 행수제한_ascen():
    row_count = 3
    is_asc = False
    # When
    df = group_by_count(keyword="자유", ascen=is_asc, n=row_count)
    # assert
    assert isinstance(df, pd.DataFrame)
    assert df.iloc[0]["president"] == "박정희"
    assert len(df) == row_count

@pytest.mark.parametrize("is_asc, president", [(True,),(False,)])
def test_정렬 및 행수제한(is_asc,president):
    row_count = 3
    is_asc = True
    # When
    df = group_by_count(keyword="자유", ascen=is_asc, n=row_count)
    # assert
    assert isinstance(df, pd.DataFrame)
    assert df.iloc[0]["president"] == "윤보선"
    assert len(df) == row_count

def test_all_count():
    # When
    df = group_by_count("자유") 
    presidents_speeches = {}
    for i in range(len(df)):
        presidents_speeches[df.iloc[i]["president"]] = df.iloc[i]["count"]
        #assert president_row.iloc[i]["count"] == s_count
    # assert
    assert presidents_speeches["박정희"] == 513 
    assert presidents_speeches["이승만"] == 438 
    assert presidents_speeches["노태우"] == 399 
    assert presidents_speeches["김대중"] == 305 
    assert presidents_speeches["문재인"] == 275
    assert presidents_speeches["김영삼"] == 274 
    assert presidents_speeches["이명박"] == 262 
    assert presidents_speeches["전두환"] == 242 
    assert presidents_speeches["노무현"] == 230 
    assert presidents_speeches["박근혜"] == 111 
    assert presidents_speeches["최규하"] == 14 
    assert presidents_speeches["윤보선"] == 1 
    
presidents_speeches = {
    "박정희": 513,
    "이승만": 438,
    "노태우": 399,
    "김대중": 305,
    "문재인": 275,
    "김영삼": 274,
    "이명박": 262,
    "전두환": 242,
    "노무현": 230,
    "박근혜": 111,
    "최규하": 14,
    "윤보선": 1
}

def test_all_count2():
    # given
    # global dict
    
    # when
    df = group_by_count("자유")
    
    # assert
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 12

    for p_name, s_count in presidents_speeches.items():
        president_row = df[df["president"] == p_name]
        assert president_row.iloc[0]["count"] == s_count


