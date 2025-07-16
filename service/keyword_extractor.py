from model.keyword_extractor import Prompt, KeywordResult
import jieba.analyse

def extract_keywords(prompt: Prompt) -> KeywordResult:
    keywords = jieba.analyse.extract_tags(prompt.text, topK=6, withWeight=False)
    return KeywordResult(keywords=keywords)