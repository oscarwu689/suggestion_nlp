from model.keyword_extractor import Prompt, KeywordResult
from service.keyword_extractor import extract_keywords
from data.keyword_extractor import _prompt_01, _keyword_result_01, _prompt_02, _keyword_result_02


def test_extract_keywords():
    result_01 = extract_keywords(_prompt_01)
    print("測試詞：", _prompt_01.text)
    print("結果：", result_01)
    print("期望：", _keyword_result_01)
    assert result_01 == _keyword_result_01

    result_02 = extract_keywords(_prompt_02)
    print("測試詞：", _prompt_02.text)
    print("結果：", result_02)
    print("期望：", _keyword_result_02)
    assert result_02 == _keyword_result_02
