from fastapi import FastAPI
import uvicorn
import jieba
from web import keyword_extractor

app = FastAPI()

app.include_router(keyword_extractor.router)

if __name__ == "__main__":
    jieba.enable_parallel(4)
    jieba.initialize()
    uvicorn.run("main:app", port=8080, reload=True)