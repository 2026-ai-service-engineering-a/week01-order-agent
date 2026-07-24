"""분식왕 주문 접수 API — v0.1 목(mock).

/order는 아직 고정 응답만 돌려줍니다. 라이브 빌드에서 에이전트 루프로 교체됩니다.
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="분식왕 주문 에이전트", version="0.1.0")


class OrderRequest(BaseModel):
    message: str


@app.post("/order")
def order(request: OrderRequest) -> dict:
    return {"message": "죄송합니다, 아직 점원이 없어요"}


# 웹 주문 화면 — API 라우트보다 뒤에 마운트해야 /order가 가려지지 않습니다
app.mount("/", StaticFiles(directory="web", html=True), name="web")
