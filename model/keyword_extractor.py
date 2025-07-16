from pydantic import BaseModel
from typing import List

class Prompt(BaseModel):
    text: str


class KeywordResult(BaseModel):
    keywords: List[str]

