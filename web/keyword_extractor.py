from fastapi import APIRouter
from model.keyword_extractor import Prompt, KeywordResult
from service.keyword_extractor import extract_keywords

router = APIRouter(prefix="/keyword_extractor")

@router.post("")
@router.post("/")
def keyword_extractor(prompt: Prompt) -> KeywordResult:
    return extract_keywords(prompt)