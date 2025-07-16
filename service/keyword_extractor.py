from model.keyword_extractor import Prompt, KeywordResult
import jieba.analyse
from errors import Missing

def extract_keywords(prompt: Prompt) -> KeywordResult:
    # check text is empty or whitespace only
    if not prompt.text or not prompt.text.strip():
        raise Missing("text can't be empty")

    keywords = jieba.analyse.extract_tags(prompt.text, topK=6, withWeight=False)
    return KeywordResult(keywords=keywords)