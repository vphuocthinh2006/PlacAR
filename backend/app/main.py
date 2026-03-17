from fastapi import FastAPI

from .config import get_settings
from .schemas import RecommendationRequest, RecommendationResponse
from .services.recommendation import basic_recommendation


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "app": settings.app_name, "env": settings.environment}


@app.post("/recommend/basic", response_model=RecommendationResponse)
def recommend_basic(payload: RecommendationRequest) -> RecommendationResponse:
    """
    Endpoint gợi ý cơ bản (chưa dùng AI/LLM).
    - Input: thông tin phòng (kích thước, loại phòng, style).
    - Output: danh sách đồ nội thất mẫu phù hợp diện tích.
    """
    return basic_recommendation(payload)

