import pytest
from errors import Missing
from model.keyword_extractor import Prompt, KeywordResult
from service.keyword_extractor import extract_keywords
from data.keyword_extractor import _prompt_01, _keyword_result_01, _prompt_02, _keyword_result_02


def test_extract_keywords():
    result_01 = extract_keywords(_prompt_01)
    assert result_01 == _keyword_result_01

    result_02 = extract_keywords(_prompt_02)
    assert result_02 == _keyword_result_02

def test_extract_keywords_whitespace_only():
    """test Missing exception"""
    prompt = Prompt(text="   \n\t  ")
    with pytest.raises(Missing) as exc_info:
        extract_keywords(prompt)
    assert exc_info.value.msg == "text can't be empty"

def test_extract_keywords_empty():
    """test Missing exception"""
    prompt = Prompt(text="")
    with pytest.raises(Missing) as exc_info:
        extract_keywords(prompt)
    assert exc_info.value.msg == "text can't be empty"