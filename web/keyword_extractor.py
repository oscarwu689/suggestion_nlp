from fastapi import APIRouter, HTTPException
from model.keyword_extractor import Prompt, KeywordResult
from service.keyword_extractor import extract_keywords
from errors import Missing

router = APIRouter(prefix="/keyword_extractor")

@router.post("")
@router.post("/")
def keyword_extractor(prompt: Prompt) -> KeywordResult:
    try:
        return extract_keywords(prompt)
    except Missing as e:
        raise HTTPException(status_code=400, detail=e.msg)